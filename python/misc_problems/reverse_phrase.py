"""

Reverse a phrase

- Take a string as input and ouput the reverse of it as a phrase
- Example: 'I have a dog' -> 'dog a have I'
- Note that spaces are included in the reversing
- Keep punctuation marks next to the words they immediately follow
    Example: 'Zoinks! This place is scary, man!' -> 'man! scary, is place This Zoinks!'

"""
import re


def reverse_phrase(string: str) -> str:
    parser = re.compile('[\w,!?¡¿\'\"\.]+|\s+')
    string_list = parser.findall(string)
    string_list.reverse()

    return ''.join(string_list)


print(reverse_phrase('I have a dog.'))
# dog. a have I
print(reverse_phrase('I have a dog\'s tail.'))
# tail. dog's a have I
print(reverse_phrase('¡Tengo un pero!'))
# pero! un ¡Tengo
print(reverse_phrase('¿Dónde está el baño?'))
# baño? el está ¿Dónde
print(reverse_phrase('Zoinks! This place is scary, man!'))
# man! scary, is place This Zoinks!
print(reverse_phrase('A bcd def!a .asb!!'))
# .asb!! def!a bcd A
