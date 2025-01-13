import Levenshtein

def calculate_CER(reference, hypothesis):
    """
    Calculate Character Error Rate (CER) between two strings.
    CER = (substitutions + deletions + insertions) / length of reference
    """
    if len(reference) == 0:
        return float('inf')  # avoid division by zero
    distance = Levenshtein.distance(reference, hypothesis)
    return distance / len(reference)


def calculate_MinCER(references, hypothesis):
    """
    Calculate Character Error Rate (CER) between two strings.
    CER = (substitutions + deletions + insertions) / length of reference
    """
    cers = [calculate_CER(reference, hypothesis) for reference in references]
    return min(cers)


def calculate_accuracy_at1(references, attempt):
    """
    Calculate accuracy of attempts against references.
    Accuracy = correct / total

    references: list[str], reference string (multiple reference strings can be provided)
    attempt: str, best attempt string
    """
    return 1 if attempt in references else 0
