# Read-only workstation inventory for Gold Coast Phase 0.
# Does not install, modify, launch, or write to Cyberpunk. Output is stdout unless -OutFile is supplied.
[CmdletBinding()]
param(
  [string]$GamePath,
  [string]$OutFile
)
$ErrorActionPreference = "SilentlyContinue"
function Get-InstalledApp([string]$NamePattern) {
  $roots = @("HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*",
             "HKLM:\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*",
             "HKCU:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*")
  foreach ($root in $roots) {
    Get-ItemProperty $root | Where-Object { $_.DisplayName -match $NamePattern } |
      Select-Object DisplayName,DisplayVersion,InstallLocation
  }
}
$candidates = @()
if ($GamePath) { $candidates += $GamePath }
$candidates += @(
  "${env:ProgramFiles(x86)}\Steam\steamapps\common\Cyberpunk 2077",
  "$env:ProgramFiles\GOG Galaxy\Games\Cyberpunk 2077",
  "C:\GOG Games\Cyberpunk 2077",
  "C:\Games\Cyberpunk 2077",
  "D:\SteamLibrary\steamapps\common\Cyberpunk 2077",
  "E:\SteamLibrary\steamapps\common\Cyberpunk 2077"
)
$found = $candidates | Where-Object { Test-Path (Join-Path $_ "bin\x64\Cyberpunk2077.exe") } | Select-Object -First 1
$game = $null
if ($found) {
  $exe = Join-Path $found "bin\x64\Cyberpunk2077.exe"
  $vi = [Diagnostics.FileVersionInfo]::GetVersionInfo($exe)
  $mods = Join-Path $found "mods"
  $red4 = Join-Path $found "red4ext\plugins"
  $scripts = Join-Path $found "r6\scripts"
  $game = [ordered]@{
    path=$found; executable=$exe; fileVersion=$vi.FileVersion; productVersion=$vi.ProductVersion
    redmodPresent=(Test-Path (Join-Path $found "tools\redmod\bin\redMod.exe"))
    modDirectories=[ordered]@{
      mods=(Test-Path $mods); red4extPlugins=(Test-Path $red4); r6Scripts=(Test-Path $scripts)
    }
    frameworkPresence=[ordered]@{
      RED4ext=(Test-Path (Join-Path $found "red4ext"))
      ArchiveXL=(Test-Path (Join-Path $found "red4ext\plugins\ArchiveXL"))
      TweakXL=(Test-Path (Join-Path $found "red4ext\plugins\TweakXL"))
      Codeware=(Test-Path (Join-Path $found "red4ext\plugins\Codeware"))
      CET=(Test-Path (Join-Path $found "bin\x64\plugins\cyber_engine_tweaks"))
      redscript=(Test-Path (Join-Path $found "r6\scripts"))
    }
  }
}
$report = [ordered]@{
  collectedAt=(Get-Date).ToString("o")
  computer=$env:COMPUTERNAME
  os=(Get-CimInstance Win32_OperatingSystem | Select-Object Caption,Version,BuildNumber)
  hardware=(Get-CimInstance Win32_ComputerSystem | Select-Object Manufacturer,Model,TotalPhysicalMemory)
  gpu=(Get-CimInstance Win32_VideoController | Select-Object Name,DriverVersion,AdapterRAM)
  cyberpunk=$game
  gamePathCandidates=$candidates
  installedTools=[ordered]@{
    WolvenKit=(Get-InstalledApp "WolvenKit")
    Blender=(Get-InstalledApp "Blender")
    EDGEkit=(Get-InstalledApp "EDGEkit")
    Python=(Get-Command python -ErrorAction SilentlyContinue | Select-Object Source)
    Git=(Get-Command git -ErrorAction SilentlyContinue | Select-Object Source)
    Node=(Get-Command node -ErrorAction SilentlyContinue | Select-Object Source)
    DotNet=(Get-Command dotnet -ErrorAction SilentlyContinue | Select-Object Source)
  }
  note="Read-only inventory; framework presence is not version or compatibility proof. Review/redact paths and machine details before sharing."
}
$json = $report | ConvertTo-Json -Depth 8
if ($OutFile) { $json | Set-Content -LiteralPath $OutFile -Encoding UTF8 }
$json
