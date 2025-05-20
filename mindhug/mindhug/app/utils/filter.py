# app/utils/filter.py

# 간단한 비속어 리스트 (필요시 더 추가 가능)
BAD_WORDS = ["바보", "멍청이", "죽어", "꺼져"]

def contains_bad_word(text: str) -> bool:
    for word in BAD_WORDS:
        if word in text:
            return True
    return False

