
<H1>Preception Coding Challenge </H1>
<H4>By: Adithya Jyothish Gopal</H4>

# answer:
![Answer](answer.png)

# Methodolgy:

&nbsp;&nbsp;&nbsp;&nbsp;I decided that the best way to tacle the problem was to split the image into two as weell as ignored the top fifth of the image, and extract the coordinates of all the the red pixels that fall within a certain range. Since most traffic cones are some shade of red to attract attention, I believe that this should work for the intents and purposes of this challenge. Not having to deal with trying to recognize shapes would add to the efficiency and speed of the program that would be crucial in decision making when controlling a car. As mentioned earlier, I also ignored the top fifth of the image, and also split the image into two while processing. This was done in order to make the line creating process easier and more efficient. Having too much irrelevant data would have made it harder to apply a proper filter on the pixel data without making the regressing model worse of a fit. The image was split into half into halves in order to more easily process the pixls in a line. I assumed that trying to create two regressing models ont he same canvas was probebly going to be an unnecessary amount of work, given that the alternetive of splitting the image would yeild equal or even better results on nearly all aspects. At the end, all I had to do was return to the original image and apply the both regression line onto this image, along with the offsets for the x and y coordinates for each line.

# What did I try initially and why I think it did not work:

&nbsp;&nbsp;&nbsp;&nbsp;Initially, I was thinking of approching the problem by traversing the image as a 2-D array and checking wether each individual pixel was red or not. The issue with this Idea was that it was extreamly tedious and inefficient. I would have had to use OpenCV anyways, or I was going to have to figre out how to classify each RGB color that fit my defenition for red. In the end, since I would end up either having to use random Github code I did not understand or use OpenCV for one pixel at a time, I decided that this was the wrong approch for either moral or efficiency reasons. Secondly, I feel like this challenge is also aimed at trying to understand how I would fit in with the preceptions team. Given that the team would have to use OpenCV, I came to the conclusion that it would be best if I learnet how to use it for this challenge.

# libraries used:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***numpy:*** A python numeric library that should come preinstalled after python3.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***PIL:*** An image manupalation library that needs to be manually installed using pip.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***OpenCV:*** A real-time computer vison python library that needs to be manually installed using pip.
