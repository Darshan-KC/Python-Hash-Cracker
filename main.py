# Use set for hash storage for O(1) lookups.
# Parallel Processing: Use Python’s multiprocessing or concurrent.futures to hash multiple words simultaneously.
# Handle Large Files: Use libraries like mmap for memory-efficient file handling.
# Progress Tracking: Use tqdm for a progress bar to monitor the cracking process.
# Prepare a test file with some hashed passwords and a matching wordlist.

import hashlib
import mmap
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

class HashCracker:
    def __init__(self, hashes_file, wordlist_file, algorithm="md5", workers=5) -> None:
        """
        Initialize the HashCracker instance.
        Args:
            hashes_file: Path to the file containing hashed passwords.
            wordlist_file: Path to the wordlist.
            algorithm: Hashing algorithm (default: md5).
            workers: Number of threads for parallel processing.
        """
        self.hashes_file = hashes_file
        self.wordlist_file = wordlist_file
        self.algorithm = algorithm
        self.workers = workers
        
        def load_file(self, file_path):
            """
            Load a file line by line using mmap for memory efficiency.
            Args:
                file_path: Path to the file.
            Yields:
                Line content stripped of whitespace.
            """
            with open(file_path, 'r') as file:
                with mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as m:
                    for line in iter(m.readline, b""):
                        yield line.decode().strip()
        

