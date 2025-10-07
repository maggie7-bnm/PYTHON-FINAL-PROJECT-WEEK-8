import streamlit as st
st.metric('Papers (filtered)', len(filtered))
st.metric('Avg abstract words', int(filtered['abstract_word_count'].mean() if len(filtered)>0 else 0))


# Publications over time
st.subheader('Publications by Year')
year_counts = filtered['year'].value_counts().sort_index()
fig1, ax1 = plt.subplots()
ax1.bar(year_counts.index.astype(str), year_counts.values)
ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Papers')
ax1.set_title('Publications by Year')
st.pyplot(fig1)


# Top journals
st.subheader('Top Journals (filtered)')
top_journals = filtered['journal'].fillna('Unknown').value_counts().head(10)
fig2, ax2 = plt.subplots(figsize=(6,4))
sns.barplot(x=top_journals.values, y=top_journals.index, ax=ax2)
ax2.set_xlabel('Number of Papers')
ax2.set_ylabel('Journal')
st.pyplot(fig2)


# Wordcloud
st.subheader('Word Cloud of Titles (filtered)')
titles = filtered['title'].dropna().astype(str).str.lower().str.replace('[^a-z0-9 ]', ' ', regex=True)
all_words = ' '.join(titles.tolist()).split()
stopwords = set(['the','and','of','in','to','for','on','with','a','an','by','from','using','sars','cov','cov19','covid','19'])
filtered_words = [w for w in all_words if len(w)>2 and w not in stopwords]
if len(filtered_words) > 0:
wc = WordCloud(width=800, height=300, background_color='white').generate(' '.join(filtered_words))
fig3, ax3 = plt.subplots(figsize=(10,4))
ax3.imshow(wc, interpolation='bilinear')
ax3.axis('off')
st.pyplot(fig3)
else:
st.info('Not enough title text to build a word cloud.')


# Show dataframe download
st.subheader('Download cleaned sample')
st.write('Save a filtered CSV of the current view:')
@st.cache_data
def to_csv(df):
return df.to_csv(index=False).encode('utf-8')


csv_bytes = to_csv(filtered)
st.download_button('Download CSV', csv_bytes, file_name='metadata_filtered.csv', mime='text/csv')


st.markdown('---')
st.write('Done. If anything breaks (file too large or memory issues), open `analysis_script.py` and set `SAMPLE_ROWS` to a smaller number to create a sample CSV first.')