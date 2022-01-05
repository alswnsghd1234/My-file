from helper import is_palindrome

# 다양한 예시에 대해 함수를 테스트합니다.
def test_is_palindrome(is_palindrome):    
    # 문자열 "madam"에 대해 테스트합니다. 리턴값은 True여야 합니다.
    assert(is_palindrome("madam") == True)

    # 아래 assert 안의 False들을 지우고 코드를 작성하면 됩니다.
    # 올바른 리턴값은 문제 설명의 함수 설계를 보고 생각해 보세요.

    # 문자열 "adam"에 대해 테스트합니다.
    assert(is_palindrome("adam") == False)

    # 빈 문자열에 대해 테스트합니다.
    assert(is_palindrome("") == True)

    # 문자열 "Step on no pets"에 대해 테스트합니다.
    assert(is_palindrome("Step on no pets") == True)

    # 문자열 "Madam, I'm Adam"에 대해 테스트합니다.
    assert(is_palindrome("Madam, I'm Adam") == True)

    # 문자열 "소주 만 병만 주소"에 대해 테스트합니다.
    assert(is_palindrome("소주 만 병만 주소") == True)

    # 문자열 "!소주 만 병만 주소?"에 대해 테스트합니다.
    assert(is_palindrome("!소주 만 병만 주소?") == True)

    # 문자열 "소주 만 병쯤만 주소"에 대해 테스트합니다.
    assert(is_palindrome("소주 만 병쯤만 주소") == False)

test_is_palindrome(is_palindrome)
