import re
input = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

def read_lines(line_input):
    sum=0
    with open("day1_input.txt","r") as file:
        for line in file:
            fst_num =""
            snd_num=""
            for symbol1 in line:
                if symbol1.isdigit():
                    fst_num = symbol1
                    break
            for symbol2 in (line)[::-1]:
                if symbol2.isdigit():
                    snd_num = symbol2
                    break

            line_num = fst_num+snd_num
            print(line_num)
            sum +=int(line_num)

    return sum


if "__main__" == __name__:
    summmary = read_lines(input) 
    print(f"Result = {summmary}")