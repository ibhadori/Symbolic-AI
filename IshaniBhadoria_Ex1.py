#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pytholog as pl

#Facts in the relations
new_kb = pl.KnowledgeBase("relations")
new_kb([
    "male(abe)",
    "female(mona)",
    "male(herb)",
    "male(homer)",
    "father(abe,herb)",
    "father(abe,homer)",
    "mother(mona,herb)",
    "mother(mona,homer)",
    "male(clancy)",
    "female(jacqueline)",
    "female(marge)",
    "female(patty)",
    "female(selama)",
    "father(clancy,marge)",
    "father(clancy,patty)",
    "father(clancy,selama)",
    "mother(jacqueline,marge)",
    "mother(jacqueline,patty)",
    "mother(jacqueline,selama)",
    "feamle(ling)",
    "mother(selama,ling)",
    "male(bart)",
    "female(lisa)",
    "female(maggie)",
    "father(homer,bart)",
    "father(homer,lisa)",
    "father(homer,maggie)",
    "mother(marge,bart)",
    "mother(marge,lisa)",
    "mother(marge,maggie)"
    #Rules for relations
    "parent(X,Y):- male(X),father(X,Y)",
    "parent(X,Y):- female(X),mother(X,Y)",
    "brother(X,Y):- male(X),father(Z,X),father(Z,Y)",
    "sister(X,Y):- female(X),female(Y),father(Z,X),father(Z,Y)",
    "grandfather(X,Y):-male(X),father(X,Z),father(Z,Y)",
    "grandfather(X,Y):-male(X),father(X,Z),mother(Z,Y)",
    "grandmother(X,Y):-female(X),mother(X,Z),mother(Z,Y)",
    "grandmother(X,Y):-female(X),mother(X,Z),father(Z,Y)",
    "grandparents(X,Y):-grandmother(X,Y);grandfather(X,Y)",
    "uncle(X,Y):- male(X),brother(X,Z),father(Z,Y)",
    "aunt(X,Y):- female(X),sister(X,Z),mother(Z,Y)",
    "sibling(X,Y):- mother(Z,X),mother(W,X),brother(Z,W)"
])


# In[2]:


new_kb.query(pl.Expr("male(abe)"))


# In[3]:


new_kb.query(pl.Expr("female(mona)"))


# In[4]:


new_kb.query(pl.Expr("mother(marge,lisa)"))


# In[5]:


new_kb.query(pl.Expr("father(marge,lisa)"))


# In[6]:


new_kb.query(pl.Expr("sister(lisa,maggie)"))


# In[7]:


new_kb.query(pl.Expr("grandfather(abe,bart)"))


# In[8]:


new_kb.query(pl.Expr("grandfather(herb,bart)"))


# In[9]:


new_kb.query(pl.Expr("brother(bart,maggie)"))


# In[10]:


new_kb.query(pl.Expr("aunt(mona,maggie)"))


# In[11]:


new_kb.query(pl.Expr("aunt(marge,ling)"))


# In[12]:


import turtle


# In[13]:


screen = turtle.Screen()


# In[14]:


screen.bgpic("family.png")


# In[15]:


player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.pendown()

move_speed = 10
turn_speed = 10

# these defs control the movement of our "turtle"
def forward():
  turtle.forward(move_speed)

def backward():
  turtle.backward(move_speed)

def left():
  turtle.left(turn_speed)
def right():
  turtle.right(turn_speed)

turtle.penup()
turtle.speed(0)
turtle.home()

# now associate the defs from above with certain keyboard events
screen.onkey(forward, "Up")
screen.onkey(backward, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()

