#%%
text = ''
for n in range(1,160):
    text += str(n) + ','

print(text)
# %%

'''
gmsh geometry2.msh -format msh2 -3 -o case/geometry.msh

gmshToFoam geometry.msh 

'''