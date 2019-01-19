
# https://www.hackerrank.com/challenges/validating-uid/problem

import re

for i in range(int(input())):
    str1 = ''.join(sorted(input()))
    try:
        assert re.search(r'[A-Z]{2}', str1)
        assert re.search(r'\d\d\d', str1)
        assert not re.search(r'[^a-zA-Z0-9]', str1)
        assert not re.search(r'(.)\1', str1)
        assert len(str1) == 10
    except:
        print('Invalid')
    else:
        print('Valid')
		