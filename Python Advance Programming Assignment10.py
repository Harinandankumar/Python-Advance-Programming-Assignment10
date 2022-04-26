#!/usr/bin/env python
# coding: utf-8

# 1. Create a function that takes the width, height and character and returns a
# picture frame as a 2D list.
# Examples
# get_frame(4, 5, &quot;#&quot;) ➞ [
# [&quot;####&quot;],
# [&quot;# #&quot;],
# [&quot;# #&quot;],
# [&quot;# #&quot;],
# [&quot;####&quot;]
# ]
# # Frame is 4 characters wide and 5 characters tall.
# 
# get_frame(10, 3, &quot;*&quot;) ➞ [
# [&quot;**********&quot;],
# [&quot;* *&quot;],
# [&quot;**********&quot;]
# ]
# # Frame is 10 characters and wide and 3 characters tall.
# 
# get_frame(2, 5, &quot;0&quot;) ➞ &quot;invalid&quot;
# # Frame&#39;s width is not more than 2.
# 
# 
# 
# 
#  
#  
#  
#  
#  Ans:-

# In[1]:


def get_frame(in_width,in_height,in_character):
    if in_width <= 2:
        print("Invalid")
    else:
        out_list = []
        for height in range(in_height):
            if height == 0 or height == in_height-1:
                out_list.append([in_width*in_character])
            else:
                out_list.append([in_character+' '*(in_width-2)+in_character])
        for ele in out_list:
            print(ele)
        print()
    
get_frame(4, 5, "#")
get_frame(10, 3, "*")
get_frame(2, 5, "0")


# 2. Write three functions:
# 1. boolean_and
# 2. boolean_or
# 3. boolean_xor
# These functions should evaluate a list of True and False values, starting from
# the leftmost element and evaluating pairwise.
# Examples
# boolean_and([True, True, False, True]) ➞ False
# # [True, True, False, True] =&gt; [True, False, True] =&gt; [False, True] =&gt; False
# boolean_or([True, True, False, False]) ➞ True
# # [True, True, False, True] =&gt; [True, False, False] =&gt; [True, False] =&gt; True
# boolean_xor([True, True, False, False]) ➞ False
# # [True, True, False, False] =&gt; [False, False, False] =&gt; [False, False] =&gt;
# False
# 
# 
# 
# 
# 
# 
# Ans:-

# In[2]:


def boolean_and(in_list):
    in_list_clone = in_list.copy()
    while len(in_list) != 1:
        x = in_list.pop(0)
        y = in_list.pop(0)
        in_list.insert(0,(x and y))
    print(f'boolean_and({in_list_clone}) ➞ {in_list[0]}')
    
def boolean_or(in_list):
    in_list_clone = in_list.copy()
    while len(in_list) != 1:
        x = in_list.pop(0)
        y = in_list.pop(0)
        in_list.insert(0,(x or y))
    print(f'boolean_or({in_list_clone}) ➞ {in_list[0]}')
    
def boolean_xor(in_list):
    in_list_clone = in_list.copy()
    while len(in_list) != 1:
        x = in_list.pop(0)
        y = in_list.pop(0)
        in_list.insert(0,(x ^ y))
    print(f'boolean_xor({in_list_clone}) ➞ {in_list[0]}')
    
boolean_and([True, True, False, True])
boolean_or([True, True, False, False])
boolean_xor([True, True, False, False])


# 3. Create a function that creates a box based on dimension n.
# Examples
# make_box(5) ➞ [
# &quot;#####&quot;,
# &quot;# #&quot;,
# &quot;# #&quot;,
# &quot;# #&quot;,
# &quot;#####&quot;
# ]
# make_box(3) ➞ [
# &quot;###&quot;,
# &quot;# #&quot;,
# &quot;###&quot;
# ]
# make_box(2) ➞ [
# &quot;##&quot;,
# &quot;##&quot;
# ]
# make_box(1) ➞ [
# &quot;#&quot;
# ]
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[3]:


def make_box(in_dimension):
    out_list = []
    for ele in range(in_dimension):
        if ele == 0 or ele == in_dimension-1:
            out_list.append('#'*in_dimension)
        else:
            out_list.append('#'+' '*(in_dimension-2)+'#')
    for ele in out_list:
        print(ele)
    print()
    
make_box(5)   
make_box(2)
make_box(1)


# 4. Given a common phrase, return False if any individual word in the phrase
# contains duplicate letters. Return True otherwise.
# Examples
# no_duplicate_letters(&quot;Fortune favours the bold.&quot;) ➞ True
# no_duplicate_letters(&quot;You can lead a horse to water, but you can&#39;t make him
# drink.&quot;) ➞ True
# no_duplicate_letters(&quot;Look before you leap.&quot;) ➞ False
# # Duplicate letters in &quot;Look&quot; and &quot;before&quot;.
# no_duplicate_letters(&quot;An apple a day keeps the doctor away.&quot;) ➞ False
# # Duplicate letters in &quot;apple&quot;, &quot;keeps&quot;, &quot;doctor&quot;, and &quot;away&quot;.
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[4]:


def no_duplicate_letters(in_string):
    out_put = None
    for ele in in_string.split(' '):
        if len(ele) == len(set(ele)):
            out_put = True
        else:
            out_put = False
            break
    print(f'no_duplicate_letters({in_string}) ➞ {out_put}')
    
no_duplicate_letters("Fortune favours the bold.")
no_duplicate_letters("You can lead a horse to water, but you can't make him drink.")
no_duplicate_letters("Look before you leap.")
no_duplicate_letters("An apple a day keeps the doctor away.")


# 5. Write a regular expression that will match the states that voted yes to
# President Trump&#39;s impeachment. You must use RegEx positive lookahead.
# Example
# txt = &quot;Texas = no, California = yes, Florida = yes, Michigan = no&quot;
# pattern = &quot;yourregularexpressionhere&quot;
# re.findall(pattern, txt) ➞ [&quot;California&quot;, &quot;Florida&quot;]
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[5]:


import re
txt = "Texas = no, California = yes, Florida = yes, Michigan = no"
pattern = r'\w+(?=\s=\syes*)'
match = re.findall(pattern,txt)
print(f're.findall{pattern,txt} ➞ {match}')

