from wordcloud import WordCloud, STOPWORDS
import wikipedia
from PIL import Image

# Define stopwords
stop_w = set(STOPWORDS)
# Get Wikipedia summary
info = wikipedia.summary("GeeksforGeeks (website)")
# Print the text for reference
print(info)
# Generate the word cloud
word_cloud = WordCloud(stopwords= stop_w).generate(info)
# Convert to image
img = word_cloud.to_image()
# Save the image in the same folder
img.save("geeksforgeeks_wordcloud.png")
# Show the image
img.show()