def int_to_binary(n):
    if n == 0:
        return "0"

    binary = ""
    is_negative = n < 0
    n = abs(n)

    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2

    if is_negative:
        binary = "-" + binary

    return binary


# 示例用法
number = 18
binary_representation = int_to_binary(number)
print(f"{number} 的二进制表示是: {binary_representation}")