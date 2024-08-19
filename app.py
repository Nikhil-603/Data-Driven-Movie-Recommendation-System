import streamlit as st
import pickle

movies=pickle.load(open("movies_list.pkl", 'rb'))
sim=pickle.load(open("similarty.pkl", 'rb'))
movies_list=movies['title'].values
# print(sim)
st.header("Movie Recommender System")
selectvalue=st.selectbox("Select movie from dropdown", movies_list)

def recommand(movi):
  index=movies[movies['title']==movi].index[0]
  distance = sorted(list(enumerate(sim[index])), reverse=True, key=lambda vector:vector[1])
  recommand_movie=[]
  for i in distance[1:6]:
    recommand_movie.append(movies.iloc[i[0]].title)
  return recommand_movie
  
if st.button("Show Recommendation"):
     movies_name = recommand(selectvalue)
     col1,col2,col3,col4,col5=st.columns(5)
     with col1:
        st.text(movies_name[0])
     with col2:
        st.text(movies_name[1])
     with col2:
        st.text(movies_name[2])
     with col4:
        st.text(movies_name[3])
     with col5:
        st.text(movies_name[4])
