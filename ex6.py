types_of_people = 10
# 格式化
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"

# 格式化
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
# 格式化
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."
# 字符串连接
print(w + e)
