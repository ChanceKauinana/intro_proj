# count_up_down.py

def setup_array(start: int, rows: int = 10, cols: int = 20):
    """
    Create a 2D array with rows x cols.
    Counts up from start until halfway through total cells, then counts back down.
    """
    total = rows * cols
    halfway = total // 2  # halfway point in the array (by cell count)

    arr = [[0 for _ in range(cols)] for _ in range(rows)]

    val = start
    for i in range(rows):
        for j in range(cols):
            idx = i * cols + j
            arr[i][j] = val

            # After filling halfway cells, reverse direction
            if idx < halfway:
                val += 1
            else:
                val -= 1

    return arr


def main():
    start = int(input("Enter starting value: "))
    arr = setup_array(start)

    # Print nicely spaced columns
    for row in arr:
        print(" ".join(f"{x:4d}" for x in row))


if __name__ == "__main__":
    main()
    