import json
import pathlib
import tempfile
import unittest
import zipfile

from scripts.package_redmod import build, validate

FIXTURE = pathlib.Path(__file__).parent / "fixtures/redmod_stub" / "GoldCoastPrototype"

class RedmodPackagingTests(unittest.TestCase):
    def test_fixture_builds_and_validates(self):
        with tempfile.TemporaryDirectory() as td:
            output = pathlib.Path(td) / "GoldCoastPrototype.zip"
            digest, count = build(FIXTURE, output)
            result = validate(output)
            self.assertEqual(result["root"], "GoldCoastPrototype")
            self.assertEqual(count, 3)
            self.assertEqual(len(digest), 64)
            self.assertTrue(output.with_suffix(".zip.sha256").is_file())

    def test_rejects_manifest_folder_mismatch(self):
        with tempfile.TemporaryDirectory() as td:
            output = pathlib.Path(td) / "bad.zip"
            with zipfile.ZipFile(output, "w") as zf:
                zf.writestr("WrongRoot/info.json", json.dumps({
                    "name": "GoldCoastPrototype", "version": "0.0.1"
                }))
            with self.assertRaises(ValueError):
                validate(output)

    def test_rejects_missing_manifest(self):
        with tempfile.TemporaryDirectory() as td:
            source = pathlib.Path(td) / "empty"
            source.mkdir()
            (source / "README.md").write_text("test", encoding="utf-8")
            with self.assertRaises(ValueError):
                build(source, pathlib.Path(td) / "out.zip")

if __name__ == "__main__":
    unittest.main()
