My highschool computer science class had a very tight-knit group of students. We often spent lunch together
working on projects. I put together this very rudimentary challenge for one of my friends who was
interested in cryptography.

The encoding works by seeding python's random library with a password. The program then iterates through all of
the text to be encoded, shifting letters through a pre-defined list of characters by random amounts. The idea is that anyone with the
right seed can very easily do the same in reverse to decode the message.

The "Decoding messages" script was sent to my friends with the encoded message already filled in. They only
needed to figure out the right password.

The python documentation itself says that its built-in random functions are not cryptographically secure,
but that wasn't the goal of this project.