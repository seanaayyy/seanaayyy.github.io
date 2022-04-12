# -M4OEP-Graphics-sander15
This project builds on the Runner Guided Project.
I've added birds that fly across the screen and flap their
wings when you press 'b', and when you move your cursor along
the grass, it will change from day to night. During the day,
the sun is in the sky and the sky is blue. At night, there is 
a crescent moon and the sky is a dark blue. At night,
bats, not birds, will fly across the screen. Below, I've noted the changes and
additions I've made to the Runner project.

## Bird class
The bird class is similar to a cloud, in that it is made of different shapes and
is drawn. It uses color and point2D from the shape class. 

### Fields
bool wingUp - notes whether a bird's wing is up or down
color fill - taken from the Shape class, is the color of the bird's body
point2D - the center coordinate of the bird's body
bool isDay - notes the time of day, affects draw function

### Important functions
default Bird constructor - This is the constructor I call in graphics.cpp.
It sets a bird's initial position at the right of the screen and at a random y
coordinate between the clouds and the tops of buildings. It's color is also chosen
at random, with red, green, and blue being anywhere from 0/255 to 255/255. 
wingUp is set to true.
moveX(double deltaX) - same functionality as Shape function of same name
void flap() - if the bird's wing is up, wingUp is changed to false and the bird
is moved up a few pixels. If the wing is down, it is changed to up (true) and 
the bird is moved down a few pixels. A timer function in graphics.cpp calls
this function on every bird to make it look like the birds are flapping
their wings.
void draw() - if isDay, draws all components of the bird. The body and head of the bird are
circles, and its beak and wings are triangles. The beak is always yellow and
the wings are set to be a little darker than the body for contrast. If isDay
is false and it is nighttime, the birds will be drawn as bats instead with
black bodies, ears instead of beaks, and will flap their wings faster.

## Additional functionality
Moving the cursor along the grass will change the time of day. On the left
half of the grass, it is daytime and the sun is showing. During the day, birds will
be drawn when 'b' is pressed. When the cursor is overlapping with the grass and 
moved to the right, the sun sets and the moon rises, the sky darkens. Bats replace
the birds at night.

## Sun
The sun is a yellow circle object, rises and sets with cursor movement on
the grass.

## Moon
The moon is a white circle object and is overlapped by another circle object,
moonShade, which is set to the sky color, so it looks like a crescent moon. It
also rises and set with cursor movement on the grass.

