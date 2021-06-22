def certification_validate(numbers):
    certification = [int(char) for char in numbers if char.isdigit()]
    if len(certification) != 7:
        return False
    if certification == certification[::-1]:
        return False
    for i in range(6, 7):
        value = sum((certification[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != certification[i]:
            return False
    return True