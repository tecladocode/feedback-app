from typing import List
import csv

FILE_NAME = 'suggestions.csv'

def save_suggestions_to_db(suggestions: List[str]):
    with open(FILE_NAME, 'w') as f:
        writer = csv.writer(f)
        for row in suggestions:
            writer.writerow([row])


def load_suggestions_from_db() -> List[str]:
    try:
        with open(FILE_NAME) as f:
            reader = csv.reader(f)
            return [row[0] for row in reader]
    except:
        return []