# :fish: Fish Module

## Contributors:

🐬 Ashley Nguyen
🐋 Erin Dominguez

## 🎓 Objectives

:octocat: Use of GitHub  
:snake: Use of Jupyter Notebooks  
:abcd: Accessing tabular data  
📈 Data visualization  
🌡️ Data on global climate change


## 📖 Content Overview

In this notebook, we will focus on examining a crucial global issue and important scientific debate about the state of global fisheries.  We will seek to reproduce some of the most widely cited examples of species collapse ever, and examine the evidence behind an influential and widely cited paper on global fisheries, [Worm et al 2006](http://doi.org/10.1126/science.1132294).  However, rather than use the limited data available to Boris Worm and colleagues in 2006, we will be drawing from the best and most recent stock asssement data available today to see how those patterns have faired. We will also conduct our own original analysis by breaking down stock collapses by region.


## The Database

We will use data from the RAM Legacy Stock Assessment Database.  We will be streaming data from <https://huggingface.co/datasets/cboettig/ram_fisheries/tree/main/v4.65>, and using ibis libraries for the majority of our analysis. One of the advantages of this is that it streams data directly from the source and will remain up to date; it also saves storage in our notebook, as it allows us to only process and store the data that is strictly necessary for our final output table.


## Science Introduction

Background abbreviated documentary that features many of the leading authors on both sides https://vimeo.com/44104959


