"""analysis_script.py


df['abstract'] = df['abstract'].fillna("")
df['abstract_word_count'] = df['abstract'].apply(lambda x: len(str(x).split()))


# Drop rows missing title or publish_time
df_clean = df.dropna(subset=['title', 'publish_time']).copy()
print(f"After dropping missing title/publish_time: {len(df_clean)} rows")


# Analysis 1: Publications by year
year_counts = df_clean['year'].value_counts().sort_index()
plt.figure(figsize=(8,5))
plt.bar(year_counts.index.astype(str), year_counts.values)
plt.title('Publications by Year')
plt.xlabel('Year')
plt.ylabel('Number of Papers')
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'publications_by_year.png'))
plt.close()
print('Saved publications_by_year.png')


# Analysis 2: Top journals
top_journals = df_clean['journal'].fillna('Unknown').value_counts().head(15)
plt.figure(figsize=(8,6))
sns.barplot(x=top_journals.values, y=top_journals.index)
plt.title('Top Journals')
plt.xlabel('Number of Papers')
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'top_journals.png'))
plt.close()
print('Saved top_journals.png')


# Analysis 3: Word frequencies in titles
print('Building word frequencies from titles...')
titles = df_clean['title'].dropna().astype(str).str.lower().str.replace('[^a-z0-9 ]', ' ', regex=True)
all_words = ' '.join(titles.tolist()).split()
# Remove short stop-like words
stopwords = set(['the','and','of','in','to','for','on','with','a','an','by','from','using','sars','cov','cov19','covid','19'])
filtered = [w for w in all_words if len(w) > 2 and w not in stopwords]
freq = Counter(filtered)
most_common = freq.most_common(50)
print('Top words in titles:', most_common[:10])


# Word Cloud
wordcloud = WordCloud(width=900, height=400, background_color='white').generate(' '.join(filtered))
plt.figure(figsize=(12,6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'wordcloud_titles.png'))
plt.close()
print('Saved wordcloud_titles.png')


# Analysis 4: Distribution by source
if 'source_x' in df_clean.columns:
source_counts = df_clean['source_x'].fillna('unknown').value_counts()
plt.figure(figsize=(8,5))
source_counts.head(10).plot(kind='bar')
plt.title('Top Sources')
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'sources.png'))
plt.close()
print('Saved sources.png')


# Save a cleaned sample CSV for the Streamlit app to use (smaller file)
sample_out = os.path.join(OUTPUT_DIR, 'metadata_clean_sample.csv')
df_clean.to_csv(sample_out, index=False)
print(f'Saved cleaned sample to {sample_out}')


print('Analysis script finished.')