def solution(phone_book):
    phone_book.sort()

    # index 활용
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            return False

    # enumerate 활용
    for i, phone_num in enumerate(phone_book[:-1]):
        if phone_num in phone_book[i + 1][:len(phone_num)]:
            return False

    return True