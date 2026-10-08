from credit_card import validate


def test_valid_visa():
    """Ensures a valid Visa number passes."""
    assert validate("4263982640269299")
    assert not validate("3263982640269291")


def test_valid_mastercard():
    """Ensures valid Mastercard numbers pass."""
    assert validate("5425233430109903")
    assert validate("5525233430109902")
    assert validate("5125233430109906")
    assert validate("2221426398264024")


def test_valid_american_express():
    """Ensures valid American Express numbers pass."""
    assert validate("374245455400126")
    assert validate("344245455400123")


def test_invalid_american_express_prefix():
    """Ensures an invalid American Express prefix fails."""
    assert not validate("377024907644532")


def test_visa_too_long():
    """Ensures a 17-digit Visa number fails."""
    assert not validate("42639826402692999")


def test_visa_too_short():
    """Ensures a 15-digit Visa number fails."""
    assert not validate("426398264026927")


def test_mastercard_too_long():
    """Ensures a 17-digit Mastercard number fails."""
    assert not validate("52252334301099064")


def test_mastercard_too_short():
    """Ensures a 15-digit Mastercard number fails."""
    assert not validate("542523343010993")


def test_amex_too_long():
    """Ensures a 16-digit American Express number fails."""
    assert not validate("3442454554001239")


def test_amex_too_short():
    """Ensures a short American Express number fails."""
    assert not validate("3542454554001")


def test_mastercard_upper_valid_boundary():
    """Ensures Mastercard upper prefix boundary 2720 passes."""
    assert validate("2720426398264020")


def test_mastercard_too_long_2720():
    """Ensures an overlength Mastercard fails."""
    assert not validate("27204263982640204")


def test_mastercard_invalid_prefix():
    """Ensures an invalid Mastercard prefix fails."""
    assert not validate("222042639826407")


def test_mastercard_below_lower_boundary():
    """Ensures prefix 2220 is rejected."""
    assert not validate("2220000000000000")


def test_mastercard_above_upper_boundary():
    """Ensures prefix 2721 is rejected."""
    assert not validate("2721000000000004")


def test_mastercard_15_digits():
    """Ensures a 15-digit Mastercard is rejected."""
    assert not validate("510000000000003")


def test_amex_16_digits():
    """Ensures a 16-digit American Express is rejected."""
    assert not validate("3400000000000000")