class Box:
    # Class Variables/member
    box_type = "Packaging Cartoon"
    color = "Brown"

    def __init__(self, side_a: int, side_b: int) -> None:
        self.side_a = side_a
        self.side_b = side_b

    def __repr__(self) -> str:
        return "<class <Box> >"

    def __str__(self) -> str:
        return f"Side A: {self.side_a}, Side B: {self.side_b}"


box1 = Box(15, 20)
print(box1)

print(box1.box_type)
print(box1.color)

# 😀static methods in Javascript
print(Box.box_type)
print(Box.color)
