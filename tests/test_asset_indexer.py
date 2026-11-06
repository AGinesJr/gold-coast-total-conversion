import importlib.util
import pathlib
import tempfile
import unittest
import yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("asset_indexer", ROOT / "scripts" / "build_asset_index.py")
asset_indexer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(asset_indexer)

BASE_RECORD = {
    "asset_id": "GC.TEST.BASE.001",
    "kind": "building",
    "game_version": "2.5",
    "source": "base_game_reference",
    "source_uri": "game-resource://example/reference",
    "provenance": "Illustrative metadata reference only; not a game asset payload.",
    "license_status": "base_game_no_redistribution",
    "reuse_decision": "reuse_in_game_only",
    "verification": "metadata_verified",
}


class AssetIndexerTests(unittest.TestCase):
    def write_record(self, folder, name, record):
        path = folder / name
        path.write_text(yaml.safe_dump(record), encoding="utf-8")
        return path

    def test_metadata_record_indexes(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = pathlib.Path(temp)
            self.write_record(folder, "one.yaml", BASE_RECORD)
            index = asset_indexer.build_index(folder)
            self.assertEqual(index["record_count"], 1)
            self.assertEqual(index["records"][0]["asset_id"], BASE_RECORD["asset_id"])
            self.assertNotIn("payload", index["records"][0])

    def test_duplicate_ids_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = pathlib.Path(temp)
            self.write_record(folder, "one.yaml", BASE_RECORD)
            second = dict(BASE_RECORD, source_uri="game-resource://another/reference")
            self.write_record(folder, "two.yaml", second)
            with self.assertRaisesRegex(ValueError, "duplicate asset_id"):
                asset_indexer.build_index(folder)

    def test_base_game_redistribution_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = pathlib.Path(temp)
            bad = dict(BASE_RECORD, license_status="approved")
            self.write_record(folder, "bad.yaml", bad)
            with self.assertRaisesRegex(ValueError, "no-redistribution"):
                asset_indexer.build_index(folder)


if __name__ == "__main__":
    unittest.main()
