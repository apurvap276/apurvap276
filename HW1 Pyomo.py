#!/usr/bin/env python
# coding: utf-8

# In[1]:


from gurobipy import *


# In[10]:


opt_mod = Model(name = " model hw1 ")  #creating optimization model


# In[13]:


x1 = opt_mod.addVar(name = 'x1', vtype = GRB.CONTINUOUS, lb=0)
x2 = opt_mod.addVar(name = 'x2', vtype = GRB.CONTINUOUS, lb=0)  #DECISION VARIABLES


# In[14]:


obj_function = 7*x1 - 2*x2
opt_mod.setObjective(obj_function, GRB.MAXIMIZE)  #DEFINING OBJECTIVE FUNCTION


# In[15]:


c1 = opt_mod.addConstr( 2*x1 + x2 <= 50, name = 'c1')
c2 = opt_mod.addConstr( x2 >= 5, name = 'c2')
c3 = opt_mod.addConstr(x1 + 3*x2 <= 75, name = 'c3')
#constraints


# In[16]:


opt_mod.optimize()
opt_mod.write("linear_model.lp")


# In[17]:


print('Objective Function Value: %f' %opt_mod.objVal)
for v in opt_mod.getVars():
    print('%s: %g'%(v.varName, v.x))


# In[ ]:




