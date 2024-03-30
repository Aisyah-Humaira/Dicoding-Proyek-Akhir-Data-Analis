import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

st.header('Dicoding Proyek Akhir Dashboard :sparkles:')
 
# Menampilkan 5 produk paling laris dan paling sedikit terjual
st.subheader("Best & Worst Performing Product")

all_product_df = pd.read_csv("all_product_df.csv")

sum_order_items_df = all_product_df.groupby(by="product_category_name_english").product_id.nunique().sort_values(ascending=False).reset_index()
sum_order_items_df.rename(columns={
    "product_category_name_english": "product name",
    "product_id": "quantity"}, inplace=True)

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))

#Best product
colors_best = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(x="quantity", y="product name", data=sum_order_items_df.head(5), palette=colors_best, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel("Number of Sales", fontsize=30)
ax[0].set_title("Best Performing Product", loc="center", fontsize=50)
ax[0].tick_params(axis='y', labelsize=35)
ax[0].tick_params(axis='x', labelsize=30)

#worst product
colors_worst = ["#f99090", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(x="quantity", y="product name", data=sum_order_items_df.sort_values(by="quantity", ascending=True).head(5), palette=colors_worst, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel("Number of Sales", fontsize=30)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Worst Performing Product", loc="center", fontsize=50)
ax[1].tick_params(axis='y', labelsize=35)
ax[1].tick_params(axis='x', labelsize=30)

st.pyplot(fig)

# Menampilkan Tipe pembayaran apa yang paling digemari pelanggan
st.subheader("Number of Customer by Payment type")

all_order_df = pd.read_csv("all_order_df.csv")

payment_type = all_order_df.groupby(by="payment_type").product_id.nunique().sort_values(ascending=False).reset_index()
payment_type.head()

plt.figure(figsize=(35, 15))
colors = ["#f990f0", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(
    x = "product_id",
    y = "payment_type",
    data = payment_type.head(),
    palette = colors
)

plt.title("Number of Customer by Payment type", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel("Number of Sales", fontsize=30)
plt.tick_params(axis='y', labelsize=35)
plt.tick_params(axis='x', labelsize=30)
st.pyplot(plt)

# Menampilkan demografi pelanggan
st.subheader("Number of Customer by City")

customers = pd.read_csv("customers.csv")

bycity_df  = customers.groupby(by="customer_city").customer_id.nunique().sort_values(ascending=False).reset_index()
bycity_df.rename(columns={
    "customer_id": "customer_count"
    }, inplace=True)

plt.figure(figsize=(35, 15))
colors = ["#90f9a0", "#D3D3D3", "#D3D3D3", "#D3D3D3","#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(
    x = "customer_count",
    y = "customer_city",
    data = bycity_df.head(7),
    palette = colors
)

plt.title("Number of Customer by City", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel("Number of Sales", fontsize=30)
plt.tick_params(axis='y', labelsize=35)
plt.tick_params(axis='x', labelsize=30)
st.pyplot(plt)

st.caption('Copyright (c) Dicoding 2023')