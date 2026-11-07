import pathlib,tempfile,unittest
from scripts.package_redmod import build
from scripts.test_install_rollback import install,uninstall
FIXTURE=pathlib.Path(__file__).parent/"fixtures"/"redmod_stub"/"GoldCoastPrototype"
class InstallRollbackTests(unittest.TestCase):
 def test_install_uninstall_preserves_unowned_file(self):
  with tempfile.TemporaryDirectory() as td:
   t=pathlib.Path(td); pkg=t/"pkg.zip"; sandbox=t/"game-sandbox"
   build(FIXTURE,pkg); sandbox.mkdir(); (sandbox/"keep.txt").write_text("user data")
   dest=install(pkg,sandbox); self.assertTrue((dest/"info.json").is_file())
   count=uninstall(sandbox,"GoldCoastPrototype"); self.assertEqual(count,3)
   self.assertFalse(dest.exists()); self.assertEqual((sandbox/"keep.txt").read_text(),"user data")
 def test_install_refuses_existing_mod(self):
  with tempfile.TemporaryDirectory() as td:
   t=pathlib.Path(td); pkg=t/"pkg.zip"; sandbox=t/"sandbox"
   build(FIXTURE,pkg); (sandbox/"mods"/"GoldCoastPrototype").mkdir(parents=True)
   with self.assertRaises(FileExistsError): install(pkg,sandbox)
 def test_uninstall_refuses_modified_owned_file(self):
  with tempfile.TemporaryDirectory() as td:
   t=pathlib.Path(td); pkg=t/"pkg.zip"; sandbox=t/"sandbox"
   build(FIXTURE,pkg); dest=install(pkg,sandbox); (dest/"info.json").write_text("changed")
   with self.assertRaises(ValueError): uninstall(sandbox,"GoldCoastPrototype")
if __name__=="__main__": unittest.main()
