# Words to images
This project is a web application created with Python in the Flask framework. The user inputs a word or sentence, and the program
converts that into an image, based on a value assigned to each letter. These values are then added together to provide a total.
The program has a range of images that is provided based on each value, i.e totals under 6 return the image of a cat.

Vowels: a, e, i, o, u = 2 points
b, j, k, q, v, x, y, z = 4 points
c, d, f, g, h, l, m, n, p, r, s, t, w = 1 point

|Input|Process|Output|
|-----|-------|------|
|User enters their name 'Dave'|D = 1, A = 2, V = 4, E = 2 total = 9|Return image assigned to a value of 9, e.g a dog|
|User enters word 'cat'|C = 1, A = 2, T = 1 total = 4| Return images assigned to a value of 4, e.g a cat|