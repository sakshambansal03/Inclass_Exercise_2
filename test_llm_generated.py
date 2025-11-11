from cs520_clean import is_palindrome, is_prime, find_max_1

# ---- Iteration 1: LLM-generated tests ----

def test_palindrome_llm_iteration1():
    assert not is_palindrome("No lemon, no melon!")
    assert not is_palindrome("Python3")
    assert is_palindrome("RaceCar")

from cs520_inclass import is_palindrome_2

def test_is_palindrome_2_cases():
    # Simple palindrome
    assert is_palindrome_2("madam")
    # Mixed case palindrome
    assert is_palindrome_2("RaceCar")
    # Palindrome with spaces and punctuation
    assert is_palindrome_2("A man, a plan, a canal: Panama")
    # Non-palindrome
    assert not is_palindrome_2("hello")
    # Empty string
    assert is_palindrome_2("")
    # Numeric palindrome
    assert is_palindrome_2("12321")


def test_is_prime_llm_iteration1():
    assert not is_prime(-5)
    assert not is_prime(0)
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(100)
    assert not is_prime(49)
    # negative and zero
    assert not is_prime(-5)
    assert not is_prime(0)
    # one is not prime
    assert not is_prime(1)
    # smallest prime
    assert is_prime(2)
    # even non-prime
    assert not is_prime(4)
    # odd prime
    assert is_prime(17)
    # composite number
    assert not is_prime(25)
    # large prime (for performance path)
    assert is_prime(101)

def test_find_max_llm_iteration1():
    # regular positive list
    assert find_max_1([1, 2, 3, 4]) == 4
    # list with all same values
    assert find_max_1([5, 5, 5]) == 5
    # list with negative values
    assert find_max_1([-10, -2, -30]) == -2
    # single-element list
    assert find_max_1([42]) == 42
    # list with large range
    assert find_max_1(list(range(-1000, 1001))) == 1000
    # empty list — should raise an error
    try:
        find_max_1([])
        assert False, "Expected ValueError for empty list"
    except ValueError:
        pass



from cs520_inclass import is_palindrome, is_prime

# ---- Iteration 2: LLM-Generated Tests ----

def test_palindrome_llm_iteration2():
    # numeric palindrome
    assert is_palindrome("12321")
    # mixed alphanumeric palindrome
    assert is_palindrome("A1b2b1a")
    # whitespace only
    assert is_palindrome("   ")
    # empty string (should be True)
    assert is_palindrome("")
    # long non-palindrome
    assert not is_palindrome("abcdefg123")
    # repeated punctuation
    assert is_palindrome("!!!aa!!!")
    # palindrome with numbers and letters combined
    assert is_palindrome("1a2b2a1")
    # very long palindrome
    long_pal = "x" * 1000
    assert is_palindrome(long_pal)
    # single-character non-alpha palindrome
    assert is_palindrome("!")
    # non-palindrome with punctuation differences
    assert not is_palindrome("madam!")



def test_is_prime_llm_iteration2():
    # negative numbers
    assert not is_prime(-7)
    assert not is_prime(-2)
    # zero and one
    assert not is_prime(0)
    assert not is_prime(1)
    # first few primes
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(5)
    # small composite
    assert not is_prime(9)
    # large prime
    assert is_prime(97)
    # large composite
    assert not is_prime(100)
        # larger primes
    assert is_prime(997)
    # large composite with multiple factors
    assert not is_prime(999)
    # edge: smallest even number > 2
    assert not is_prime(4)
    # test 2-digit even composite
    assert not is_prime(42)
    # big non-prime with multiple small factors
    assert not is_prime(120)
