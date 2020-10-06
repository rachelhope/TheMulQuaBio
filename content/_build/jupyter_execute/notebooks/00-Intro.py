#!/usr/bin/env python
# coding: utf-8

# # Introduction <span class="tocSkip"></span> <a name="chap:Intro"></a>
# 
# > *It is hard for me to say confidently that, after fifty more years of explosive growth of computer science, there will still be a lot of fascinating unsolved problems at peoples' fingertips, that it won't be pretty much working on refinements of well-explored things. Maybe all of the simple stuff and the really great stuff has been discovered. It may not be true, but I can't predict an unending growth. I can't be as confident about computer science as I can about biology. Biology easily has 500 years of exciting problems to work on, it's at that level.*
# >
# > — *Donald Knuth*
# 

# ## About these notes
#     
# These online notes have emerged from the development of content for modules on Biological Computing taught in various past and present courses at the Department of Life Sciences, Imperial College London. These courses include Year 1 & 2 Computational Biostatistics modules at the South Kensington Campus, the Computational Methods in Ecology and Evolution [(CMEE) Masters program](http://www.imperial.ac.uk/life-sciences/postgraduate/masters-courses/computational-methods-in-ecology-and-evolution/) at the Silwood Park Campus, the Quantitative Methods in Ecology and Evolution Centre for Doctoral Training ([QMEE CDT](https://www.imperial.ac.uk/qmee-cdt/)), and the training workshops of the [VectorBiTE RCN](http://vectorbite.org).
# 
# Different subsets of this document will be covered in different courses. Please look up your respective course guidebooks/handbooks to determine when the modules covered in these notes are scheduled in your course. You will be given instructions about which sections are covered in your course.
# 
# All the chapters of these notes are written as [jupyter](Appendix-JupyIntro.ipynb) notebooks. Each chapter/notebook is accompanied by data and code on which you can practice your skills in your own time and during practical sessions.  These materials are available (and will be updated regularly) at a [git repository](https://mhasoba.github.io/TheMulQuaBio/). We use git for hosting this course's materials because we want to version-control this course's content, which is constantly evolving to keep up with changing programming/computing technologies. That is, we are treating this course as any computing project that needs to be regularly updated and improved. Changes to the notes and content will also be made based upon student feedback. Blackboard is just not set up to handle dynamic updating and version control of this sort! 
# 
# If you do not use git, you may download the code, data, these notes, and other course materials from the [repository](https://github.com/mhasoba/TheMulQuaBio) at one go look for the green "Clone or Download" button and then clicking on the "Download repository" link. You can then unzip the downloaded .zip and grab the files you need.
# 
# ---
# 
# ![image](./graphics/programming.png)
# <small> <center>(Source: [http://xkcd.com/974](http://xkcd.com/974)) 
# </center></small>
# 
# ---
# 
# It is important that you work through the exercises and problems in each chapter. This document does not tell you every single thing you need to know to perform the exercises in it. In programming and computing, you learn faster by trying to solve problems (including computer crashes!) on your own, often by liberally googling the problem!
# 
# 
# ### Learning goals
# 
# The goal of this book is to teach you to become (or at least show you the path towards becoming) a competent quantitative biologist. A large part of this involves learning computer programming. Why do biologists
# need to write computer programs? Here are some (hopefully compelling!) reasons:
# 
# * Short of fieldwork, programs can do anything (that can be specified). In fact, even fieldwork, if you could one day *program* a robot to do it for you <sup>[1](#intro:robot)</sup>!
# 
# * As such, no software is typically available to perform exactly the analysis you are planning. You should be unhappy if you are trying to shoehorn your data into methods that don't quite seem right.
# 
# * Biological problems and datasets are some of the most complicated imaginable. Programming permits success despite
# complexity through precise specification and modularization of complicated analyses.
# 
# * Modularity – programming allows you to break up your complex analysis in smaller pieces, yet keep all the pieces in a single, functional analysis.
# 
# * Reproducibility – you (or someone else) can just re-run the code to reproduce your analysis. This is also the key to maintaining scientific accountability, integrity, and accuracy.
# 
# * Organised thinking – writing code requires you to do this!
# 
# * Career prospects – good, scientific coders are in short supply in all fields, but most definitely in biology!
# 
# There are several hundred programming languages currently available – which ones should a biologist choose? Ideally, a quantitative biologist would multilingual, knowing:
# 
# 1. A *fast*, compiled (or semi-compiled) 'procedural' language like `C`
# 
# 2. A modern, easy-to-write, interpreted (or semi-compiled) language that is still quite fast, like `python`
# 
# 3. A mathematical/statistical software with programming and graphing capabilities like `R`
# 
# And all these because one language doesn't fit all purposes. Therefore you will learn a few different languages in this course — hopefully, just the right number! Among the languages you will learn here — ` python`, `R`, and `C` are three of the [most popular currently](https://www.tiobe.com/tiobe-index) (also [see this page](https://spectrum.ieee.org/static/interactive-the-top-programming-languages-2018)), and with good reasons.
# 
# Our goal is to teach you not just programming, but also good computing practices. In this course, you will write plenty of code, deal with different data files, and produce text and graphic outputs. You will learn to keep your project and coursework organized in logical, efficient, error-free and reproducible *workflows* (that's a mouthful, but an important mouthful).
# 
# ## Some guidelines, conventions and rules
# 
# ### Beware the dark forces
# 
# You will NOT be using spreadsheet software (e.g., Excel) on this course. There are times when you will feel the pull of the dark side (ahem!), and imagine a more "comfortable" world where you are mouse-clicking your way happily though Excel-based data manipulations and analyses. NO! You will be doing yourself a disservice. On the
# long-ish run you will be much better off visualizing and manipulating data on your computer using a programming language like R. This is something you will learn, young [*padawan*](http://starwars.wikia.com/wiki/Padawan)!
# 
# ### Keep your workflow organized
# 
# In the following chapters, you will practice many examples where you are required to write large blocks of code. Please get into the habit of writing code into text files with an appropriate extension (e.g., `.R` for `R` code, `.py` for `python` code, etc.). Furthermore, please keep all your code files organized in one or more directories (e.g., named `Code`!). Similarly, some of these scripts will take data files as inputs, and output some results in the form of text or graphics. Please keep these inputs and outputs organized as well, in
# separate directories (e.g., named `Data` and ` Results`) respectively. Your instructor(s) will help you get set up and abide by this "workflow".
# 
# ![image](graphics/workflow.png)
# <small> 
#     <center>(Source: http://xkcd.com/1172) 
#                 Logical workflows are important, but don't get married to yours!
#      </center>
# </small>
# 
# 
# 
# ---
# 
# ### Conventions used in this document
# 
# Throughout these sessions, directory paths will be specified in UNIX (Mac, Linux) style, using `/` instead of the `\` used in Windows. Also, in general, we will be using [relative paths](https://en.wikipedia.org/wiki/Path_(computing)) throughout the exercises and practicals (more on this later, but google it!).
# 
# You will find all command line/console arguments, code snippets and output in coloured boxes like this:

# In[1]:


# Some code here!


# You will type the commands/code that you see in such boxes into the relevant command line (don't copy-paste - you likely need all the command / syntax typing practice you can get !). 
# 
# Note that the commandline prompt you will see on your own terminal/console will vary with the programming language: `$` for UNIX, `>>>` for Python, `>` for R, etc. 
# 
# Also note that:
# 
# $\star$ Lines marked with a star like this will be specific instructions for you to follow
# 
# 
# And there will be tips that you should pay particular attention to, which will appear like this:  
# 
# ---
# 
# > **This is a tip** 
# 
# ---
# 
# 
# > **So here's your first (and perhaps most important) tip:**  This document does not tell you every single thing you need to know to perform the exercises in it. In programming and computing, you learn faster by trying to solve problems on your own. The contemporary way to do this is to google the problem! Some suggestions: 
# * Your typical modus operandi should be to google the main keywords along the programming language name (e.g., "unix mv vs cp" or "R create empty dataframe"). 
# * Look for [stackoverflow](https://stackoverflow.com/) or [stackexchange](https://stackexchange.com/) based results in particular. Look for number of endorsements for both the question that has been asked, and for its answer.
# * Be selective - there will often be multiple solutions to the same issue or problem - don't just blindly use the first one you find. 
# * Also, every time a mysterious, geeky-sounding term like "relative path" or "version control" appears, please google it as well!
# 
# ---
# 
# 
# ### To IDE or not to IDE?
# 
# As you embark on your journey to becoming a competent practitioner of biological computing, you will be faced with a Hamletian question: "To IDE or not to IDE" (anagram alert!). OK, maybe not that dramatic or Hamletian...
# 
# An interactive Development Environment (IDE) is a text editor with frills that can make life easy by auto-formatting code, running code though the terminal or command line, allowing a graphic view of the workspace (your active functions, variables, etc.), graphic debugging and profiling (you will see these delightful things later), and allowing integrated version control (e.g., using `git`). You will benefit a lot if you use a code editor that can also offer an IDE (e.g., emacs, vim, geany, atom). At the very least, your IDE should offer:
# 
# * Auto-indentation
# 
# * Automatic code wrapping (e.g., keeping lines $<$80 characters long)
# 
# * Syntax highlighting (e.g., commands vs. variables)
# 
# * Code folding (fold large blocks of code, say an entire function or loop)
# 
# * Keyboard control of commenting/uncommenting, code wrapping, etc.
# 
# * Embedded terminal / shell / commandline console
# 
# * Sending commands to terminal / shell
# 
# And if you end up using multiple programming languages, you will want an IDE that can handle them. For example, `RStudio` is great for R, but cannot handle other languages. I use visual studio `code`, which has many plugins that make multi-language (multilingual!) code development much easier. Other good options are `atom`, `vim` or `emacs`. The last two have a steeper learning curve, but are very powerful once you have mastered them. 
# 
# ### Assessment
# 
# Your computing coursework may be assessed. If you have been told that it will, please see [this Appendix](Appendix-Assessment.ipynb) if you are a *Masters student*. If you are an *Undergrad student*, you may have a computer based test, the format for which will be explained to you elsewhere.

# **Footnotes**
# 
# <a name="intro:robot">1</a>: That way you can traipse around the forest catching rare butterflies and frogs while the robot does the boring data collecting for you
