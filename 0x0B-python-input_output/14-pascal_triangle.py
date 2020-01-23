def pascal_triangle(n):
    """
    Create a function def pascal_triangle(n): that returns a list
    of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = []
    row = [1]
    triangle.append(row)

    for i in range(1, n):
        prev = triangle[i - 1]
        row = []
        row.append(1)

        for j in range(1, i):
            row.append(prev[j - 1] + prev[j])
        row.append(1)
        triangle.append(row)

    return triangle
