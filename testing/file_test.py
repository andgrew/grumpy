f = open('/tmp/foo', 'w')
assert f.softspace == 0

f.softspace = 1
assert f.softspace == 1

try:
    f.softspace = 'deadbeef'
except TypeError as e:
    assert str(e) == "an int is required. Field 'file.softspace' cannot store a 'str' value", e