#!/usr/bin/env python
# coding: utf-8

# In[16]:


from flask import Flask, request, render_template


# In[17]:


app = Flask(__name__)


# In[18]:


import joblib


# In[19]:


@app.route("/", methods=["GET", "POST"])
def index():
  if request.method=="POST":
    purchases = request.form.get("purchases")
    print(purchases)
    suppcard = request.form.get("suppcard")
    print(suppcard)

    cart = joblib.load("CART")
    result1 = cart.predict([[int(purchases), int(suppcard)]])

    rf = joblib.load("RF")
    result2 = rf.predict([[int(purchases), int(suppcard)]])

    gb = joblib.load("GB")
    result3 = gb.predict([[int(purchases), int(suppcard)]])
    
    return(render_template("index.html", result1=result1, result2=result2, result3=result3))
  else:
    return(render_template("index.html", result1="Loaded", result2="Loaded", result3="Loaded"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:





# In[ ]:




