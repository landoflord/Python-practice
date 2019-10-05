import sys
Zero = ["   000   ",
        "  0   0  ",
        "0       0",
        "0       0",
        "0       0",
        "  0   0  ",
        "   000   "]
One =  ["    1    ",
        "  111     ",
        "    1    ",
        "    1    ",
        "    1    ",
        "    1    ",
        " 1111111 "]
Two =  ["   222   ",
        " 2     2 ",
        "       2 ",
        "     2   ",
        "   2     ",
        " 2       ",
        " 2222222 "]
Three =["   333   ",
        " 3     3 ",
        "       3",
        "    333  ",
        "       3 ",
        " 3     3 ",
        "   333   "]
Four = ["    4    ",
        "   44    ",
        "  4 4    ",
        " 4  4    ",
        "4444444  ",
        "    4    ",
        "    4    "]
Five = [" 5555555 ",
        " 5       ",
        " 5       ",
        " 5555555 ",
        "       5",
        "       5 ",
        " 5555555 "]
Six =  [" 6666666 ",
        " 6       ",
        " 6       ",
        " 6666666 ",
        " 6     6",
        " 6     6 ",
        " 6666666 "]
Seven =[" 7777777 ",
        "       7 ",
        "      7  ",
        "     7   ",
        "    7    ",
        "   7     ",
        "  7      "]
Eight =["   888   ",
        " 8     8 ",
        " 8     8 ",
        "  88888  ",
        " 8     8 ",
        " 8     8 ",
        "   888   "]
Nine = ["   999   ",
        " 9     9 ",
        " 9     9 ",
        "  99999  ",
        "     9   ",
        "    9    ",
        "   9    "]
Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]
stroutput = ['','','','','','','']
while True:
    line = input("integer:")
    if line:
        try:
            for i in line:
                j = 0
                for x in Digits[int(i)]:
                        stroutput [j] += x
                        j= j+1
        except ValueError as err:
            print(err)
            continue
    else:
        break
for i in stroutput:
    print(i)