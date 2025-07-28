# Colors

This is a discussion about color palettes that could be used to represent notes.

Considerations include:
* Relevant color palettes that are widely used 
* Having color palettes which are color blind
* Considering adjusting saturation or luminance to express octave changes in notes 
* Optimising perceptual distinctiveness
* Having some sort of ordering or no?
* Aspects of colors: paleness, brightness, contrast, saturation, luminance, ...

> Consider using shapes as well to describe notes

## Questions and Answers 

### What is RGB system? What is HSL? What are the difference?

RGB (Red, Green, Blue): A color model where colors are created by combining red, green, and blue light in varying intensities (0–255). Common in screens and digital displays.

HSL (Hue, Saturation, Lightness):
A cylindrical color model that represents colors by:
* Hue: Color type (0–360°, like red, blue, etc.)
* Saturation: Color intensity (0–100%)
* Lightness: Brightness (0–100%)

Key Differences:
* Model Basis: RGB is based on light intensity; HSL is based on human perception of color.
* Ease of Use: HSL is more intuitive for adjusting color shades and tints.
* Use Cases: RGB for technical rendering; HSL for design and editing.

> Lightness (brightness) vs luminance (perceived brightness)

### What is RGB system? What is HSL? What are the difference?

💧 Saturation in RGB:
* **Saturation** = Color intensity or purity.
* In RGB, **high saturation** means big differences between R, G, and B.
* **Low saturation** = R, G, and B values get closer → color looks more gray.

Example:
* Pure red: `RGB(255, 0, 0)` → vivid
* Less saturated: `RGB(200, 50, 50)` → dull red
* No saturation: `RGB(128, 128, 128)` → gray


💡 Luminance in RGB:
* Luminance refers to the perceived brightness of a color (how bright a color appears)
* In RGB, it’s influenced by the overall level of red, green, and blue — but not equally: Green contributes the most, then red, then blue (due to how our eyes perceive brightness). More technical details and formulas [here](https://en.wikipedia.org/wiki/Relative_luminance) and [here](https://stackoverflow.com/questions/596216/formula-to-determine-perceived-brightness-of-rgb-color).
* An approximate formula here: `(0.2126*R + 0.7152*G + 0.0722*B)` (the human eyeball is most sensitive to green light, less to red and least to blue)

Example:
* Medium blue: `RGB(0, 0, 200)`
* Brighter (more luminance): `RGB(100, 100, 255)`
* Darker (less luminance): `RGB(0, 0, 50)`

🔁 Summary:
| Change       | RGB Effect                 | Result            |
| ------------ | -------------------------- | ----------------- |
| ↑ Saturation | RGB values spread apart    | More vivid color  |
| ↓ Saturation | RGB values move closer     | Duller, more gray |
| ↑ Luminance  | RGB values move toward 255 | Lighter color     |
| ↓ Luminance  | RGB values move toward 0   | Darker color      |

### What are some popular color palettes for increased perceptual distinctiveness? 

Here are 
* Color Universal Design (CUD) Palette: Developed for color vision accessibility (esp. red-green color blindness).
* Paul Tol’s Color Schemes: Designed for data visualization with attention to colorblind safety, Balanced hues, good for categories or sequences (Cover a wide range of the color wheel, while avoiding clustering too many colors around the) ([website](https://sronpersonalpages.nl/~pault/))
* Tableau Color Palette: Widely used in business dashboards, Designed for readability and distinction across categories
* Okabe & Ito Palette: Colorblind-safe (tested with deuteranopia and protanopia), 8 colors with good spacing in color space
* Material Design Color Palette (Google): Designed for UI use, strong emphasis on contrast and consistency, Less optimal for data visualization but good for perceptual clarity in interfaces ([website](https://m2.material.io/design/color/the-color-system.html))
* ColorBrewer2: Tool for generating colorblind-safe and print-friendly palettes, offers Qualitative palettes (for categories), Sequential palettes (for gradients) and Diverging palettes (for bipolar data)


Best Practices:
* Use no more than 8–10 categorical colors for clarity
* Avoid adjacent colors that are similar in hue and lightness
* Test for color vision deficiencies (using tools like Coblis or Sim Daltonism)
* Ensure contrast ratio for accessibility (WCAG guidelines recommend 4.5:1 for normal text)


#### How is the contrast ration measured?

The formula is:

Contrast Ratio = (L1 + 0.05) / (L2 + 0.05)
 
where L1 (and L2) is the relative luminance of the lighter (and darker) color

Given a color in sRGB (hex or RGB):
1. Normalize RGB components between 0 and 1 (0–255 → 0–1)
2. Apply gamma correction, [resource here](https://www.cambridgeincolour.com/tutorials/gamma-correction.htm)
3. Compute luminance as mentioned before



### What is the difference between RGB and RYB? What about CYM?

RGB (Red, Green, Blue):
* Additive color model used for digital screens and light.
* Colors mix by adding light, producing white when combined fully.
* Primary colors: Red, Green, Blue.

RYB (Red, Yellow, Blue):
* Traditional subtractive color model used in art and painting.
* Colors mix by subtracting light (pigments), producing darker colors when combined.
* Primary colors: Red, Yellow, Blue.

Extra info:
* RGB is an additive color model, used to mix light. You start start with black (no light) and add red/blue/green light to create color. Screens (TVs, computer monitors, phone displays) use this model. 
* CMY is a subtractive model, used to mix pigments or dyes. Printers use this model. Mixing Cyan/Magenta/Yellow creates a brighter and larger range of colors than RYB.
* RGB and CMY are essntially opposites.
* RYB is a subtractive color model, meaning you start from white and add color to subtract light. Newton’s work on color (in the 17th century) was focused on pigments and paints. It became artist's primary color system. When mixing pigments, where combining colors subtracts wavelengths from light.

* YT video for CMY vs RYB: [Controversial Color Theory: RYB vs CMY Color Wheel - What are the REAL Primary Colors?](https://youtu.be/yRQmV4XYmqI)
    * There are even more primary color systems: Psychological primaries, natural color system and imaginary primaries. All of them with differrent approaches/diagrams/primary colors.
    * The deep problem is that color is not circular. It's only wavelenghts of light. Wheels are for humans to organise them conceptually.

* [Figma color names](https://www.figma.com/colors/mango/) 


### What is CMYK? How is it related to RGB?

CMYK is a subtractive color model (meaning colors are created by subtracting light using pigment) primarily used in color printing. It stands for Cyan, Magenta, Yellow, and Key (Black) — the four ink colors used in color printing. Combining all four produces deep, rich blacks and a wide range of printed colors.


CMYK and RGB are opposite color models used for different mediums:

* RGB (Red, Green, Blue) is additive and used for screens—colors are created by adding light.
* CMYK is subtractive and used for printing—colors are created by subtracting light with ink.

### What is HSV? How is it related to HSL?

HSL and HSV are both cylindrical color models used in digital design, but they differ in how they represent color's lightness and saturation. HSL (Hue, Saturation, Lightness) is more intuitive for picking colors because lightness directly controls the perceived brightness, while HSV (Hue, Saturation, Value/Brightness) is often preferred for image processing because its value component more closely reflects how humans perceive brightness. [Wiki](https://en.wikipedia.org/wiki/HSL_and_HSV).

### Online tools

* [Color wheels](https://www.w3schools.com/colors/colors_wheels.asp)
* [Color wheel in Canvas](https://www.canva.com/colors/color-wheel/)
* [Relative luminance in Colors](http://www.workwithcolor.com/color-luminance-2233.htm)
    * You can lighten or darken a color by adjusting its lightness value, but lightness is not the only dimension to consider for luminance. That is because each hue naturally has an individual luminance value.

> A certain color can be defined by hue (0° - 360°), saturation (0% - 100%) and lightness (0% - 100%). Luminance on the other hand is a measure to describe the perceived brightness of a color

* [Color Picker](https://www.hslpicker.com/)
* [Luminance Calculator](https://contrastchecker.online/color-relative-luminance-calculator)

## List of colors

### Color wheel hex codes

The 12 Main Colors of RGB (check [here](https://www.1728.org/RGB3a.htm) and [here](https://www.1728.org/RGB3.htm)):
```
#FF0000 (RED) | hsl(0, 0.5, 1.0) | hsv(0, 1.0, 1.0)  | luminance = 0.2126
#FF8000 (ORANGE) | hsl(30, 0.5, 1.0) | hsv(30, 1.0, 1.0) | luminance = 0.3669834297
#FFFF00 (YELLOW) | hsl(60, 0.5, 1.0) | hsv(60, 1.0, 1.0) | luminance = 0.9278
#80FF00 (CHART / CHARTREUSE) | hsl(90, 0.5, 1.0) | hsv(90, 1.0, 1.0) | luminance = 0.7610919423
#00FF00 (GREEN) | hsl(120, 0.5, 1.0) | hsv(120, 1.0, 1.0) | luminance = 0.7152
#00FF80 (SPRIN / SPRINGGGREEN) | hsl(150, 0.5, 1.0) | hsv(150, 1.0, 1.0) | luminance = 0.7307851281
#00FFFF (CYAN) | hsl(180, 0.5, 1.0) | hsv(180, 1.0, 1.0) | luminance = 0.7874
#0080FF (AZURE) | hsl(210, 0.5, 1.0) | hsv(210, 1.0, 1.0) | luminance = 0.2265834297
#0000FF (BLUE) | hsl(240, 0.5, 1.0) | hsv(240, 1.0, 1.0) | luminance = 0.0722
#8000FF (VIOLET) | hsl(270, 0.5, 1.0) | hsv(270, 1.0, 1.0) | luminance = 0.1180919423
#FF00FF (MAGENTA) | hsl(300, 0.5, 1.0) | hsv(300, 1.0, 1.0) | luminance = 0.2848
#FF0080 (ROSE) | hsl(360, 0.5, 1.0) | hsv(360, 1.0, 1.0) | luminance = 0.2281851281
```


The 12 Main Colors of RYB (according to [w3](https://www.w3schools.com/colors/colors_wheels.asp))
```
#FE2712 (RED)
#FC600A (R-O)
#FB9902 (ORANGE)
#FCCC1A (Y-O)
#FEFE33 (YELLOW)
#B2D732 (Y-G)
#66B032 (GREEN)
#347C98 (B-G)
#0247FE (BLUE)
#4424D6 (B-P)
#8601AF (PURPLE)
#C21460 (R-P)
```

Original color names for RYB wheel  

RYB All colors with names (according to [here](https://color.fandom.com/wiki/RYB_Primary,_Secondary,_Tertiary,_and_Quaternary_colors)):
```
#FF0000 (Red) 
#FF2000 (Scarlet)
#FF4000 (Vermilion)
#FF6000 (Tangerine)
#FF8000 (Orange)
#FF9F00 (Mango)
#FFBF00 (Amber)
#FFDF00 (Saffron)
#FFFF00 (Yellow)
#BFFF00 (Lime)
#80FF00 (Chartreuse)
#40FF00 (Apple Green)
#00FF00 (Green)
#008040 (Viridian)
#008080 (Teal)
#004080 (Cobalt)
#0000FF (Blue)
#200080 (Indigo)
#400080 (Violet) (Dark Violet)
#600080 (Amethyst)
#800080 (Purple)
#A40B83 (Fuchsia)
#C71585 (Magenta)
#800020 (Crimson)
```

* What if I adjust for luminance?

### Lists of distinctive color palettes

> Having a color wheel can be beneficial, as it gives an intuitive classification. The problem is that the shades of green are hard to distinguish. Plus the luminance of the color wheel is not fixed.

* [Paul Tol color schemes pdf](https://sronpersonalpages.nl/~pault/data/colourschemes.pdf)

* [An Optimum 16 Color Palette](http://alumni.media.mit.edu/~wad/color/palette.html)
Using 4 neutral colors and 12 colors with different hues, saturations (`[("Black", (0, 0, 0)),("Dk. Gray", (87, 87, 87)),("Red", (173, 35, 35)),("Blue", (42, 75, 215)),("Green", (29, 105, 20)),("Brown", (129, 74, 25)),("Purple", (129, 38, 192)),("Lt. Gray", (160, 160, 160)),("Lt. Green", (129, 197, 122)),("Lt. Blue", (157, 175, 255)),("Cyan", (41, 208, 208)),("Orange", (255, 146, 51)),("Yellow", (255, 238, 51)),("Tan", (233, 222, 187))]`)

* [K. Kelly (1965): Twenty-two colors of maximum contrast]()

* [A Colour Alphabet and the Limits of Colour Coding]()

* [List of 20 Simple, Distinct Colors](https://sashamaps.net/docs/resources/20-colors/)

* [tableu colors](https://jrnold.github.io/ggthemes/reference/tableau_color_pal.html)
    * subset of classic 20
    * classic traffic light
    * classic cyclical

* [ColorBrewer](https://colorbrewer2.org/#type=qualitative&scheme=Paired&n=12)
The first 12-class qualitative
```
#a6cee3
#1f78b4
#b2df8a
#33a02c
#fb9a99
#e31a1c
#fdbf6f
#ff7f00
#cab2d6
#6a3d9a
#ffff99
#b15928
```

The second 12-class qualitative (more pale):
```
#8dd3c7
#ffffb3
#bebada
#fb8072
#80b1d3
#fdb462
#b3de69
#fccde5
#d9d9d9
#bc80bd
#ccebc5
#ffed6f
```


### Experiments

As mentioned before, the basic RGBs:
```
#FF0000 (RED) | hsl(0, 0.5, 1.0) | hsv(0, 1.0, 1.0)  | luminance = 0.212
#FF8000 (ORANGE) | hsl(30, 0.5, 1.0) | hsv(30, 1.0, 1.0) | luminance = 0.367
#FFFF00 (YELLOW) | hsl(60, 0.5, 1.0) | hsv(60, 1.0, 1.0) | luminance = 0.928
#80FF00 (CHART / CHARTREUSE) | hsl(90, 0.5, 1.0) | hsv(90, 1.0, 1.0) | luminance = 0.761
#00FF00 (GREEN) | hsl(120, 0.5, 1.0) | hsv(120, 1.0, 1.0) | luminance = 0.715
#00FF80 (SPRIN / SPRINGGGREEN) | hsl(150, 0.5, 1.0) | hsv(150, 1.0, 1.0) | luminance = 0.730
#00FFFF (CYAN) | hsl(180, 0.5, 1.0) | hsv(180, 1.0, 1.0) | luminance = 0.787
#0080FF (AZURE) | hsl(210, 0.5, 1.0) | hsv(210, 1.0, 1.0) | luminance = 0.226
#0000FF (BLUE) | hsl(240, 0.5, 1.0) | hsv(240, 1.0, 1.0) | luminance = 0.0722
#8000FF (VIOLET) | hsl(270, 0.5, 1.0) | hsv(270, 1.0, 1.0) | luminance = 0.118
#FF00FF (MAGENTA) | hsl(300, 0.5, 1.0) | hsv(300, 1.0, 1.0) | luminance = 0.285
#FF0080 (ROSE) | hsl(360, 0.5, 1.0) | hsv(360, 1.0, 1.0) | luminance = 0.228
```

Let's adjust the value (the s metric in hsv) so as to drop luminance in color (to be similar to blue color, which has the minumum, around 0.1 to 0.2):
```
#b30000 (RED) | hsv(0, 1.0, 0.7)
#994d00 (ORANGE) | hsv(30, 1.0, 0.6) 
#666600 (YELLOW) | hsv(60, 1.0, 0.4) 
#408000 (CHART / CHARTREUSE) | hsv(90, 1.0, 0.5) 
#008000 (GREEN) | hsv(120, 1.0, 0.5) 
#008040 (SPRIN / SPRINGGGREEN) | hsv(150, 1.0, 0.5) 
#008080 (CYAN) | hsv(180, 1.0, 0.5) 
#006cd9 (AZURE) | hsv(210, 1.0, 0.85) 
#0000FF (BLUE) | hsv(240, 1.0, 1.0) 
#8000ff (VIOLET) | hsv(270, 1.0, 1.0) 
#cc00cc (MAGENTA) | hsv(300, 1.0, 0.8) 
#e60073 (ROSE) | hsv(360, 1.0, 0.9) 
```

I don't think it makes that much sense, but maybe dropping v (for chart and spring, which are similar to green) (and for green which is too bright) would help with distinguishing them.

```
#FF0000 (RED) | hsl(0, 0.5, 1.0) 
#FF8000 (ORANGE) | hsl(30, 0.5, 1.0) 
#e6e600 (YELLOW) | hsl(60, 0.5, 0.95) 
#79f200 (CHART / CHARTREUSE) | hsl(90, 0.5, 0.95) 
#00FF00 (GREEN) | hsl(120, 0.5, 1.0) 
#00e673 (SPRIN / SPRINGGGREEN) | hsl(150, 0.5, 0.95) 
#00FFFF (CYAN) | hsl(180, 0.5, 1.0) 
#0080FF (AZURE) | hsl(210, 0.5, 1.0) 
#0000FF (BLUE) | hsl(240, 0.5, 1.0) 
#8000FF (VIOLET) | hsl(270, 0.5, 1.0) 
#FF00FF (MAGENTA) | hsl(300, 0.5, 1.0) 
#FF0080 (ROSE) | hsl(360, 0.5, 1.0) 
```

What if I alternate with deeper (lower v) colors:
```
#bf0000 (RED) | hsl(0, 0.5, 0.75) 
#FF8000 (ORANGE) | hsl(30, 0.5, 1.0) 
#bfbf00 (YELLOW) | hsl(60, 0.5, 0.75) 
#80FF00 (CHART / CHARTREUSE) | hsl(90, 0.5, 1.0) 
#00bf00 (GREEN) | hsl(120, 0.5, 0.75) 
#00FF80 (SPRIN / SPRINGGGREEN) | hsl(150, 0.5, 1.0) 
#00bfbf (CYAN) | hsl(180, 0.5, 0.75) 
#0080FF (AZURE) | hsl(210, 0.5, 1.0) 
#0000bf (BLUE) | hsl(240, 0.5, 0.75) 
#8000FF (VIOLET) | hsl(270, 0.5, 1.0) 
#bf00bf (MAGENTA) | hsl(300, 0.5, 0.75) 
#FF0080 (ROSE) | hsl(360, 0.5, 1.0) 
```

What if we make more steps between red and green (and less later on?). Kind of combine RYB and RGB.
Equally separated values.
00 - 56 - aa - ff
```
#ff0000
#ff5600
#ffaa00
#ffff00
#aaff00
#56ff00
#00ff00
#00ff56
#00ffaa
#00ffff
#00aaff
#0056ff
#0000ff
#5600ff
#aa00ff
#ff00ff
#ff00aa
#ff0056
#ff0000
```

Now using that, we just skip some values:
```
#ff0000 do
#ff5600 ka
#ffaa00 re
#ffff00 ni
#00ff00 mo
#00ffff fa
#0080ff ze
#0000ff si
#8000ff po
#ff00ff la
#ff00aa ve
#ff0056 ti
#ff0000 do
```

Green is too powerful, so drop it's power to maximum aa (not ff). Therefore the rest of the colors will take charge.
That means (red and blue: `00-80-ff` and green: `00-56-aa`, which is 2/3 of the maximum)
```
#ff0000 do 
#ff5600 ka
#ffaa00 re
#80aa00 ni
#00aa00 mo
#00aa80 fa
#00aaff ze
#0056ff si
#0000ff po
#8000ff la
#ff00ff ve
#ff0080 ti
#ff0000 do
```

A second way is switching values simulaneously:
```
#ffaa00 
    / downgrade values
#aa5600 
    / switch 
#56aa00 
    / upgrade values
#aaff00 
    / hop
#00ffaa 
    / downgrade values
#00aa56
    / switch 
#0056aa
    / upgrade values
#00aaff
    / hop
#aa00ff
    / downgrade values
#5600aa
    / switch 
#aa0056
    / upgrade values
#ff00aa
    / hop
#ffaa00
```

Or what if we split in four levels `00-40-80-bf-ff` but ff drops while 00 rise?
```
#ff0000 (red)
#bf4000
#808000
#40bf00
#00ff00 (green)
#00bf40
#008080
#0040bf
#0000ff (blue)
#4000bf
#800080
#bf0040
#ff0000
```

What if we adjust the power of green and red?
What if we want to lower the power of green? `00-40-80` in general
```
#ff0000
#ff4000
#ff8000
#808000
#008000
#008080
#0080ff
#0040ff
#0000ff
#8000ff
#ff00ff
#ff0080
#ff0000
```

What if we added all three colors at some points. To make it asymmetric:
`00-40-80-bf-ff` or `00-55-aa-ff`
```
#ffbf80
#bf8040
#804000
#008040
#40bf80
#80ffbf
#bf80ff
#8040bf
#400080

#804000
#008040
#400080
#408000
```


Combine colors in 3 levels? (`3*3*3=27` - 3 neutral = 24)
```
#000000 (000)
#000080 (001)
#0000ff (002)
#008000 (010)
#008080 (011)
#0080ff (012)
#00ff00 (020)
#00ff80 (021)
#00ffff (022)
#800000 (100)
#800080 (101)
#8000ff (102)
#808000 (110)
#808080 (111)
#8080ff (112)
#80ff00 (120)
#80ff80 (121)
#80ffff (122)
#ff0000 (200)
#ff0080 (201)
#ff00ff (202)
#ff8000 (210)
#ff8080 (211)
#ff80ff (212)
#ffff00 (220)
#ffff80 (221)
#ffffff (222)


there are three digits. A is the initial ace. L is the lucky zero (it's left or right/direction will be fixed). U is the unlucky 0.
* increase A & L
* increase U & L
* decrase U & A
* decrase L & A

001,012,122,021, 010,120,221,210, 100,201,212,102
001,102,212,201, 100,210,221,120, 010,021,122,012

#800000 (100) (red)
#ff8000 (210)
#ffff80 (221) 
#80ff00 (120)
#008000 (010) (green)
#00ff80 (021)
#80ffff (122)
#0080ff (012)
#000080 (001) (blue)
#8000ff (102)
#ff80ff (212)
#ff0080 (201)
```
> this is one of the most complex but also one of my favourites

Combine colors in 4 levels? (`4*4*4=64` choices - 4 neutrals)
```
#ffaa55 (321)
#ff55aa (312)
#aaff55 (231)
#aa55ff (213)
#55aaff (123)
#55ffaa (132)

#ff5555 (311)
#55ff55 (131)
#5555ff (113)

#ffaaaa (322)
#aaffaa (232)
#aaaaff (223)

#aa5500 (210)
#aa0055 (201)
#55aa00 (120)
#5500aa (102)
#0055aa (012)
#00aa55 (021)
```

Combining three colors?
```
#ff8000
#ff0080
#00ff80
#80ff00
#0080ff
#8000ff

#ff8080
#80ff80
#8080ff

#ff0000
#ffff00
#00ff00
#00ffff
#0000ff
#ff00ff
```




We could also use the [natural color system](https://en.wikipedia.org/wiki/Natural_Color_System) (which uses four colors) and the three version/intonations/saturations (deeper, mid, light), to name all notes:
* Green (#009F6B)
* Red (#C40233)
* Yellow (#FFD300)
* Blue (#0087BD)
Essentially, it's a RYGB circle. It's propriatery, so not really open and usable. 


[Color charts](https://en.wikipedia.org/wiki/Color_chart)

* this [site](https://www.greenleafblueberry.com/blogs/news/modern-primary-colors) has a lovely picture, where the greens are more easily seperable.