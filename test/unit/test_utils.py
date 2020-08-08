from typing import List
import tempfile


def test_list_files():
    """Ensure files list is not empty."""
    from anom.utils.io import list_files
    with tempfile.TemporaryDirectory() as dirpath:
        example_file = open(dirpath + "/example.txt", "w")
        example_file.write("........")
        example_file.close()
        files: List[str] = list_files(dirpath)
        assert files
