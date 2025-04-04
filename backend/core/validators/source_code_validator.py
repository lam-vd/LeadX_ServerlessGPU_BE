import ast

def validate_source_code(source_code):
    if not source_code.strip():
        raise ValueError("source_code_cannot_be_empty")

    dangerous_keywords = ["os.system", "subprocess", "eval", "exec"]
    for keyword in dangerous_keywords:
        if keyword in source_code:
            raise ValueError(f"source_code_contains_dangerous_keyword: {keyword}")

    return True