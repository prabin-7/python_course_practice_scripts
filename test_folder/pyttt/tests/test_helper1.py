from my_src.helper1 import subtract1               #pytt.my_src.helper1 garda didnt work with pytest so we need relative pathing  (cause found __inti__.py not in pyttt)
#pytt is made a module then  relative import works with pytest
#esle when pytt is not a module need to do absolute import
def test_subtract():
    assert subtract1(1,1)==0