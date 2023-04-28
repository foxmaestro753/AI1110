ball = int(input("Enter the number of balls"))
red = int(input("Enter the number of red balls : "))
black = int(input("Enter the number of black balls : "))

while ball != (red+black) :
    red = int(input("Enter the number of red balls : "))
    black = int(input("Enter the number of black balls : "))

answer1,answer2,answer3,count = 0,0,0,0
for k in range(1,ball+1,1):
    for j in range(1,ball+1,1):
        if k<=red and j<=red :
            answer1+=1
        if k>red and j<=red :
            answer2+=1
        if k<=red and j>red : 
            answer3+=1

for k in range(1,ball+1,1):
    for j in range(1,ball+1,1):
        count+=1

print(f"2.1 answer = {answer1/count}, 2.2 answer = {answer2/count}, 2.3 answer = {(answer2+answer3)/count}")