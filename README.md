# Manipulating joint probability densities in python

The final part of the question is the most tedious one to solve by hand.  It asks:

The joint probability density function for the pair of continuous random variables (X,Y) is:

![](https://render.githubusercontent.com/render/math?math=f(x,y)=k(x^2y^2%2Bxy^3)\quad\textrm{for}\quad\1<x<2\quad\textrm{and}\quad\0<y<3)

(5) Compute the correlation coefficient between the two variables.

To do this you need to compute all the following integrals: ![](https://render.githubusercontent.com/render/math?math=\mathbb{E}(X)), ![](https://render.githubusercontent.com/render/math?math=\mathbb{E}(Y)), ![](https://render.githubusercontent.com/render/math?math=\textrm{var}(X)), ![](https://render.githubusercontent.com/render/math?math=\textrm{var}(Y)) and ![](https://render.githubusercontent.com/render/math?math=\textrm{cov}(X,Y)) (sigh...).  To complete the exercise you thus need to calculate all of these using SymPy.  Notice that I have not defined a k symbol for you because I would like you to use the value that we determined in part 2; namely, that k=8/411.  Notice, furthermore, that when you set a variable such as `px` equal P(X=x) you can then use `px` when you set `ex` equal to ![](https://render.githubusercontent.com/render/math?math=\mathbb{E}(X)).
