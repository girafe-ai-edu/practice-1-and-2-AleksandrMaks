# %% [markdown]
# ## Tasks №1 and Tasks №2 
# 
# Jupiter notebook is an interactive development environment with live code. It shows a visualization of the work. If a developer wants to look at a graph or formula, he writes the necessary command in the appropriate cell. This approach saves time and helps to avoid mistakes.
# 
# 
# 

# %% [markdown]
# ## Useful features  
# 
# Magic commands that work in ipython that can help you run and analyze data in jupyter notebook. They add special functionality that is not easy to achieve with Python code or the Jupyter notebook interface.
# 
# All maigc commonds %lsmagic

# %% [markdown]
# ### Working with cells
# The code is executed inside the cells, sequentially based on the number to the left of the cell.

# %%

a=1
print('Output  а variable = ',a)

# %%
b=2
print('Output b variable b = ',b)

# %%
#We can output variables from previously started cells
print(a,b)

# %% [markdown]
# ### Task №1
# There are dimensions width (a) and length of the room (b) and height of the walls (c), output the volume of the room in m3 with a floating point

# %%
a = 3
b = 4
c = 3

print(float(a*b*c))



# %% [markdown]
# ### Task №2
# There is a list of list_v values, output a list without duplicate values
# 

# %%
list_v = [2,2,3,4,5,0,0]

#code here

print(list_v)

# %%



