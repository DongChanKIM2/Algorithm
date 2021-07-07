def solution(phone_book):
    phone_dict = {}
    answer = True
    for number in phone_book:
        phone_dict[number] = 1

    for phoneNumber in phone_book:
        temp = ''
        for number in phoneNumber:
            temp += number
            if temp in phone_dict and temp != phoneNumber:
                answer = False
                return answer

    return answer

