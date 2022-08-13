import streamlit as st
import pandas as pd

df = pd.read_csv('recom.csv',index_col = 0)
product_df = pd.read_csv('ProductRaw.csv')
id_list = df['customer_id'].values[:100]
def get_info(id):
    check = product_df.loc[product_df['item_id']==id]
    if len(check) == 1:
        my_item = {
            'name':check['name'].values[0],
            'des':check['description'].values[0],
            'rating':check['rating'].values[0],
            'price':check['price'].values[0],
            'listprice':check['list_price'].values[0],
            'img': check['image'].values[0]
        }
        return my_item
    return None
    




st.title("Recommendation system (customer's rating based - Collaborative Filtering)")
st.write("This is a project I built in June 2022, which is creating a recommedation system based on customer's ratings. I chose Tiki.vn to crawl necesary data. You might be quite familiar with recommedation things, when you are probably browsing on Youtube or Nexlif, or online store, and the actual website will give you recommendation products somewhere in the webpage.")
st.image('img/Tiki recommendation.png')
st.image('img/Youtube recommendations.png')
st.write('In this page, you will be able to choose the ID of the customer (we all have IDs of customers whenever they visit our page), then provide them a list of recommended items/products, and FE team can put it somewhere in the actual page.')
st.write('---')

def onchange():

    cus_res = eval(df.loc[df['customer_id']==int(myselect)]['rec'].values[0])
    # st.write(my_op)

    for i in cus_res:
        my_product = get_info(i[0])
        p_name = my_product['name']
        p_des = my_product['des']
        p_rating = my_product['rating']
        p_price = my_product['price']
        p_lprice = my_product['listprice']
        p_img = my_product['img']


        col1, col2 = container.columns([1,2])
        with col1:
            st.image(p_img,width=150)
        # col2.write(p_des)
        with col2:
            st.write(f'<h4 style="color:blue;">{p_name}</h4>',unsafe_allow_html = True)
            st.write(f'<p>&#9733;{p_rating}</p>',unsafe_allow_html = True)
            st.write(f'<h3><s style="color:red;">{p_lprice}</s> <b style="color:green;">{p_price}</b></h3>',unsafe_allow_html = True)
            # st.write(p_lprice)
        container.write('---')



# with st.sidebar:
#     # with st.echo():
#     mybutton = st.button('Learn more about the system')
    # recommend = st.button('Go to recommendation system')
myselect = st.selectbox('Pick one customer ID, and recommended list will be shown above.',id_list,on_change=onchange)
container = st.container()


# if recommend:  
with container:
    st.write(f'<p>Recommended products for customer with ID:  <b style="font-size:25px;">{myselect}</b></p>',unsafe_allow_html = True)
    
# if mybutton:



