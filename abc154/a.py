balls_color1, balls_color2 = input().split()
balls_count1, balls_count2 = map(int, input().split())

balls = {
    balls_color1: balls_count1,
    balls_color2: balls_count2
}

trash = input()
balls[trash] -= 1

print(balls_count1, balls_count2)