"""
Program Name: Lab 3 - Word Count
Author: Colin Lee
Purpose: Read a selected text file, count how often each
word appears, and display the results alphabetically.
Starter Code: No starter code was provided.
Date: October 1, 2026
"""

from pathlib import Path
import string


class WordAnalyzer:
    """Analyzes word frequencies in a text file."""
 
    def __init__(self, filepath):
        """Initialize the file path and word counts."""
        self.__filepath = Path(filepath)
        self.__frequencies = {}

    def process_file(self):
        """Read the file and count word frequencies."""
        try:
            if not self.__filepath.exists():
                raise FileNotFoundError

            translation_table = str.maketrans(
                "", "", string.punctuation
            )

            with self.__filepath.open("r", encoding="utf-8") as file:
                for line in file:
                    line = line.lower()
                    line = line.translate(translation_table)
                    words = line.split()

                    for word in words:
                        if word in self.__frequencies:
                            self.__frequencies[word] += 1
                        else:
                            self.__frequencies[word] = 1

            return True

        except FileNotFoundError:
            print("Error: The selected file was not found.")
            return False

    def print_report(self):
        """Display word frequencies alphabetically."""
        sorted_words = sorted(self.__frequencies.keys())

        for word in sorted_words:
            count = self.__frequencies[word]
            print(f"{word:<20} :: {count}")


def main():
        """Display the menu and handle user choices."""
        base_path = Path(__file__).resolve().parent

        files = {
            "1": ("Princess of Mars", base_path / "princess_mars.txt"),
            "2": ("Tarzan", base_path / "Tarzan.txt"),
            "3": ("Treasure Island", base_path / "treasure_isalnd.txt"),
            "4": ("The Count of Monte Cristo", base_path / "monte_cristo.txt")
        }

        while True:
            print("\n--- Word Analyzer ---")
            print("Please select a file to analyze:")

            for choice, (title, filepath) in files.items():
                print(f"{choice}. {title}")

            print("5, Exit")

            choice = input("\nEnter your choice (1-5): ")

            if choice == "5":
                print("Goodbye!")
                break

            elif choice in files:
                title, filepath = files[choice]
                print("f\nProcessing '{filepath.name}'...")

                analyzer = WordAnalyzer(str(filepath))

                if analyzer.process_file():
                    analyzer.print_report()

            else:
                print("\nInvalid choice. Please select from 1-5.")

            input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
    main()




