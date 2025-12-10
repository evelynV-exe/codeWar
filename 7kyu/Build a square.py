def generate_shape(n):
    lines = []
    for i in range(n):
        line = "+" * n
        lines.append(line)
    return "\n".join(lines)
print(generate_shape(3))