from madlib_cli.madlib import read_template,parse,merge

def testRead():
    actual = read_template()
    expected = open('assets/sample_template.txt','r').read()
    assert expected == actual

def testParse():
    actual = parse("I the {Adjective } and {Adjective} {A First Name}")
    expected = (['Adjective', 'Adjective', 'A First Name'], 'I the  {} and  {}  {}')
    assert expected == actual

def testmerge():
    actual= merge('I the {} and {} {}',['smart','cute','joudi'])
    expected = "I the smart and cute joudi"
    assert expected == actual
