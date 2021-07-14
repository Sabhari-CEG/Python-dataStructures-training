#The namedtuple method returns a tuple-like object that has fields accessible
# with named indexes as well as the integer indexes of normal tuples.
from collections import namedtuple
if __name__ == '__main__':
    space = namedtuple('space','x def z',rename=True)
    s1 = space(x=2.0,_1=4.0,z=10.0)
    print("The values in the tuple\n",s1.x,s1._1,s1.z)
    sl = [4,5,6]
    s2 = space._make(sl)
    print("The make function\n",s2)
    d = s2._asdict()
    print("The given dictionary\n",d)
    s2 = s2._replace(x=10)
    print("after replacing\n",s2)