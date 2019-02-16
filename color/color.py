class RGBColor:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        return "rgb({},{},{})".format(self.r, self.g, self.b)

    def as_hex(self):
        return HexColor("#%02x%02x%02x" % (self.r, self.g, self.b))

    def as_cmyk(self):
        k = min(1-self.r, 1-self.g, 1-self.b)
        c = (1-self.r-k)/(1-k)
        m = (1-self.g-k)/(1-k)
        y = (1-self.b-k)/(1-k)

        return CMYKColor(c, m, y, k)

    def as_hsl(self):
        r_scaled = self.r/255
        g_scaled = self.g/255
        b_scaled = self.b/255

        c_max = max(r_scaled, g_scaled, b_scaled)
        c_min = min(r_scaled, g_scaled, b_scaled)

        lightness = (c_max + c_min) / 2

        if c_max == c_min:
            hue = 0
            saturation = 0
        else:
            delta = c_max - c_min

            hue = {
                r_scaled: 60*((g_scaled-b_scaled)/delta % 6),
                g_scaled: 60*((b_scaled-r_scaled)/delta+2),
                b_scaled: 60*((r_scaled-g_scaled)/delta+4),
            }[c_max]

            saturation = delta/(1-abs(2*lightness-1))

        return HSLColor(hue, saturation, lightness)

    def as_rgb(self):
        return self

    def as_rgba(self):
        return [self.r, self.g, self.b, self.a]

    def complementary(self):
        hsl = self.as_hsl(self.r, self.g, self.b)
        comp_hue = hsl.h + 180
        if comp_hue > 360:
            comp_hue = comp_hue - 360

        hsl.h = comp_hue

        return hsl

    def analogous(self):
        pass


class RGBAColor:
    def __init__(self, r, g, b, a=255):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __str__(self):
        return "rgba({},{},{},{})".format(self.r, self.g, self.b, self.a)


class HexColor:
    def __init__(self, hexcode):
        self.code =hexcode

    def __str__(self):
        return self.code


class CMYKColor:
    def __init__(self, c, m, y, k):
        self.c = c
        self.m = m
        self.y = y
        self.k = k

    def __str__(self):
        return "cmyk({},{},{},{})".format(self.c, self.m, self.y, self.k)


class HSLColor:
    def __init__(self, h, s, l):
        self.h = h
        self.s = s
        self.l = l

    def __str__(self):
        return "hsl({},{},{})".format(self.h, self.s, self.l)


if __name__ == "__main__":
    color = RGBColor(10, 10, 13)
    print(color)
    print(color.as_cmyk())
    print(color.as_hsl())
    print(color.as_hex())
