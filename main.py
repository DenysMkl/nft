from string import ascii_lowercase as al
def solution(s: str) -> str:
    prev_letter = ''
    mass_of_slice = []
    curr_slice = ''
    for i in s:
        if prev_letter + i not in al:
            mass_of_slice.append(curr_slice)
            curr_slice = i
        else:
            curr_slice += i
        prev_letter = i

    mass_of_slice.append(curr_slice)

    return ''.join(i[::-1] for i in mass_of_slice)

print(solution('pqrsxdef'))