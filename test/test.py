import re2 as r

def main():
    concatenate()
    repetition()
    disjunction()
    grouping()
    concat_zero()
    concat_disj()
    concat_group()
    zero_rep_disj()
    zero_rep_group()
    disj_group()
    concat_zero_disj()
    concat_zero_group()
    concat_disj_group()
    zero_disj_group()
    all_core_func()
    return(1)

def concatenate():
    matches = r.findall(r'[b-f][a-z]', 'alemfntz')
    assert matches == ['em', 'fn'], "Did not pass concatenation test1"


    matches = r.findall(r'[b-f][a-z]', 'alamdntz')
    assert matches == ['dn'], "Did not pass concatenation test2"


    matches = r.findall(r'[b-f][a-z]', 'alamntz')
    assert matches == [], "Did not pass concatenation test3"


    matches = r.findall(r'[b-f][a-z]', 'alamntz')
    assert not matches == ['ef'], "Did not pass concatenation test4"

def repetition():
    assert(r.match(r'[a-z]*', 'abcde'))
    assert(r.match(r'[a-z]*', 'ABCDE'))
    assert(r.match(r'a*', 'aaaaaa'))
    assert(r.match(r'a*','baaaaa'))

def disjunction():
    assert(r.match(r'[a-c]|[d-f]', 'e'))
    assert(r.match(r'[a-c]|[d-f]', 'z') == None)
    assert(r.match(r'a|b', 'a'))
    assert(r.match(r'a|b','c') == None)

def grouping():
    assert(r.match(r'([a-c])([d-f])', 'be'))
    assert(r.match(r'([a-c])([d-f])', 'ab') == None)
    assert(r.match(r'(a)(b)','ab'))
    assert(r.match(r'(a)(b)','ba') == None)

def concat_zero():
    assert(r.match(r'[a-f][a-z]*','earth'))
    assert(r.match(r'[a-f][a-z]*','zebra') == None)

def concat_disj():
    assert(r.match(r'[a-c][d-f]|az','ad'))
    assert(r.match(r'[a-c][d-f]|az','py') == None)

def concat_group():
    assert(r.match(r'(ll)(o)', 'llo'))
    assert(r.match(r'(ll)(o)', 'dead') == None)

def zero_rep_disj():
    assert(r.match(r'[b-z]*|[b-z]','project'))
    assert(r.match(r'[b-z]*|[b-z]','a'))

def zero_rep_group():
    assert(r.match(r'(a)([a-z])*','aardvark'))
    assert(r.match(r'(a)([a-z])*','mother') == None)

def disj_group():
    assert(r.match(r'([a-c]+)|([h-z])','r'))
    assert(r.match(r'([a-c]+)|([h-z])','d') == None)

def concat_zero_disj():
    assert(r.match(r'a[a-z]*| b[a-z]','aardvark'))
    assert(r.match(r'a[a-z]*| b[a-z]','foo') == None)

def concat_zero_group():
    assert(r.match(r'(a*[a-z])([a-z])','bb'))
    assert(r.match(r'(a*[a-z])([a-z])','i') == None)

def concat_disj_group():
    assert(r.match(r'(a[a-z])|(b[a-z])','apple'))
    assert(r.match(r'(a[a-z])|(b[a-z])','goofy') == None)

def zero_disj_group():
    assert(r.match(r'(hi)([a-z]*)(bob|sarah)','hiiiiiiiiibob'))
    assert(r.match(r'(hi)([a-z]*)(bob|sarah)','misarah') == None)

def all_core_func():
    assert(r.match(r'(a[a-z]*)|(b[a-z])','apapap'))
    assert(r.match(r'(a[a-z]*)|(b[a-z])','cup') == None)
    assert(r.match(r'(hello)(sir)|(yeehaw)*partner','yeehawyeehawpartner'))
    assert(r.match(r'(hello)(sir)|(yeehaw)*partner','hello') == None)
    

if __name__ == "__main__":
    main()