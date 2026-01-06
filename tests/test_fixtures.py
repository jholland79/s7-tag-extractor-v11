"""Tests for sample Step 7 project fixtures.

This module tests that the required sample project files are available
for integration testing of the S7 tag extractor.
"""

from pathlib import Path


FIXTURES_DIR = Path(__file__).parent / "fixtures"
SAMPLE_PROJECT_DIR = FIXTURES_DIR / "sample_project"


class TestSampleProjectFixtures:
    """Tests verifying sample S7 project is properly set up."""

    def test_symlist_dbf_exists_in_sample_project(self):
        """Sample project should contain SYMLIST.DBF for symbol table testing.

        The SYMLIST.DBF file is essential for extracting symbol names,
        addresses, and comments from Step 7 projects.
        """
        # Arrange
        expected_file = SAMPLE_PROJECT_DIR / "YDBs" / "Snap7" / "SYMLIST.DBF"

        # Act & Assert
        assert expected_file.exists(), (
            f"SYMLIST.DBF not found at {expected_file}. "
            "Download sample project from: "
            "https://github.com/SCADACS/snap7/tree/master/examples/Step%207/Snap7"
        )
