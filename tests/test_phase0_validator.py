import pathlib, tempfile, unittest, yaml
from scripts.validate_phase0 import validate_task, validate_asset_record, validate_toolchain, ROOT

class Phase0ValidatorTests(unittest.TestCase):
    def test_repository_task_contracts_are_valid(self):
        for path in (ROOT/"agent/tasks").glob("*.yaml"):
            self.assertTrue(validate_task(path).startswith("GC-"))

    def test_task_missing_required_field_is_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            path=pathlib.Path(td)/"bad.yaml"
            path.write_text(yaml.safe_dump({"task_id":"GC-P0-9999"}),encoding="utf-8")
            with self.assertRaises(ValueError): validate_task(path)

    def test_task_must_forbid_main_push(self):
        with tempfile.TemporaryDirectory() as td:
            path=pathlib.Path(td)/"bad.yaml"
            task=yaml.safe_load((ROOT/"agent/tasks/GC-P0-0001-pipeline-bootstrap.yaml").read_text())
            task["forbidden_actions"]=[]
            path.write_text(yaml.safe_dump(task),encoding="utf-8")
            with self.assertRaises(ValueError): validate_task(path)

    def test_toolchain_unknown_values_are_allowed_in_discovery(self):
        count=validate_toolchain(ROOT/"config/toolchain.lock.yaml")
        self.assertGreater(count,0)

    def test_asset_catalog_sample_validates(self):
        for path in (ROOT/"catalogs/samples").glob("*.yaml"):
            self.assertTrue(validate_asset_record(path))

if __name__ == "__main__": unittest.main()
