# Words to images
## Description
This project is a web application created with Python in the Flask framework. The user inputs a word or sentence, and the program
converts that into an image, based on a value assigned to each letter. These values are then added together to provide a total.
The program has a range of images that is provided based on each value, i.e totals under 6 return the image of a cat.

Points:
* a, e, i, o, u = 2 points
* b, j, k, q, v, x, y, z = 4 points
* c, d, f, g, h, l, m, n, p, r, s, t, w = 1 point

|Input|Process|Output|
|-----|-------|------|
|User enters their name 'Dave'|D = 1, A = 2, V = 4, E = 2 total = 9|Return image assigned to a value of 9, e.g a dog|
|User enters word 'cat'|C = 1, A = 2, T = 1 total = 4| Return images assigned to a value of 4, e.g a cat|

## Requirements
As this is a web application, the user will not be required to download any specific software etc. However, they will need internet access via their device. The user will be required to input words comprised of the latin alphabet.

## What the program does
1. User opens web browser on their device
2. User goes to the web page
3. User inputs a word or phrase into the words form
4. The program assigns a number to each letter and adds the total together
5. The program scans the list of images, each of which are linked to a range of numbers i.e the cat image is for values under 6
6. The program finds the image that correlates to this particular value 
7. The program returns the image.

## Edge cases
The program only assigns values to letters from the latin alphabet. All other special characters, including punctuation and blank spaces, will be ignored. If the user does not enter at least one letter, the program will return an error message, asking the user to input a word. The program will not be case sensitive.

