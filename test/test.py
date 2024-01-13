def reverse(self):
    return self[::-1]

# Monkey Patching
str.reverse = reverse

# Usage
my_string = "Hello, World!"
print(my_string.reverse()) 