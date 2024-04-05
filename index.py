import math


def get_angle(distance_back):
    inside_post = math.sqrt(distance_back**2 + 32.2**2)
    outside_post = math.sqrt(distance_back**2 + 37.8**2)

    # Cosine Rule a^ = b^ + c^ - 2bcCosA

    before_equals = (5.6**2) - (inside_post**2) - (outside_post**2)

    after_equals = 2 * inside_post * outside_post

    denominator = after_equals * -1

    before_equals2 = before_equals / denominator

    angle = math.degrees(math.acos(before_equals2))

    return angle


out = open("out.txt", "w")

for x in range(1, 101):
    print(x, "metres: ", get_angle(x))
    out.write(str(get_angle(x)) + "\n")

out.close()
