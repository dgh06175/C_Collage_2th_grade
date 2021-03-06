import re
txt_data = 'Python was conceived in the late 1980s[35] by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) \
in the Netherlands as a successor to the ABC language (itself inspired by SETL),[36] capable of exception handling \
and interfacing with the Amoeba operating system.[8] Its implementation began in December 1989.[37] \
Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, \
when he announced his "permanent vacation" from his responsibilities as Python\'s Benevolent Dictator For Life, \
a title the Python community bestowed upon him to reflect his long-term commitment as the project\'s chief decision-maker.\
[38] He now shares his leadership as a member of a five-person steering council.[39][40][41] \
In January 2019, active Python core developers elected Brett Cannon, \
Nick Coghlan, Barry Warsaw, Carol Willing and Van Rossum to a five-member "Steering Council" \
to lead the project.[42]\nPython 2.0 was released on 16 October 2000 with many major new features, \
including a cycle-detecting garbage collector and support for Unicode.[43]\nPython 3.0 was released on 3 December 2008. \
It was a major revision of the language that is not completely backward-compatible.[44] Many of its major features were \
backported to Python 2.6.x[45] and 2.7.x version series. Releases of Python 3 include the 2to3 utility, which automates \
(at least partially) the translation of Python 2 code to Python 3.[46]\nPython 2.7\'s end-of-life date was initially set \
at 2015 then postponed to 2020 out of concern that a large body of existing code could not easily be forward-ported to Python 3.'

while 36020:
    start_str = input('시작 문자열 입력: ')
    end_str = input('끝 문자열 입력: ')
    if start_str.isalpha() & end_str.isalpha():
        break
    print('잘못 입력하셨습니다. 다시 입력해주세요\n')

print(start_str + '로 시작하고 ' + end_str + '로 끝나는 단어 목록')
for v in re.findall(r'\b'+ start_str + r'\w*' + end_str + r'\b', txt_data):
    print(v)
