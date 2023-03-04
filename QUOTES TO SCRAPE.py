#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


import bs4


# In[10]:


res = requests.get('https://quotes.toscrape.com')

res.text
# In[11]:


soup=bs4.BeautifulSoup(res.text,'lxml')


# In[12]:


soup


# In[14]:


soup.select('.author')


# In[15]:


authors=set()
for name in soup.select(".author"):
    authors.add(name.text)
    


# In[16]:


authors


# In[19]:


quotes = [] 
for quote in soup.select('.text'):
    quotes.append(quote.text)


# In[20]:


quotes


# In[21]:


for item in soup.select('.tag-item'):
    print(item.text)


# In[22]:


url='https://quotes.toscrape.com/page/'


# In[25]:


authors = set()
for page in range(1,10):
    page_url = url+str(page)
    res = requests.get(page_url)
    soup = bs4.BeautifulSoup(res.text, "lxml")
    for name in soup.select(".author"):
        authors.add(name.text)
    
    


# In[26]:


authors


# In[27]:


page_still_valid = True
authors = set()
page=1


while page_still_valid:
    page_url = url+str(page)
    res = requests.get(page_url)
    
    if "No quotes found!" in res.text:
        break
    soup = bs4.BeautifulSoup(res.text, "lxml")
    for name in soup.select(".author"):
        authors.add(name.text)
    
    
    page = page+1


# In[28]:


authors


# In[ ]:




