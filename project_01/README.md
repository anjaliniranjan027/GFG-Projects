# GFG Projects

A collection of projects created while learning and experimenting with Python and data visualization.

---

## 📌 Project 01 — GeeksforGeeks Word Cloud

This project generates a **Word Cloud** using text fetched from the GeeksforGeeks Wikipedia page.  
The word cloud highlights the most frequently used words visually.

### 🛠️ Features
- Fetches summary from Wikipedia using the `wikipedia` Python module.
- Generates a word cloud using the `wordcloud` library.
- Saves the generated image locally for later use.

### 📷 Output
The output image (`geeksforgeeks_wordcloud.png`) will look something like this:

![Word Cloud](geeksforgeeks_wordcloud.png)

### 📦 Requirements
Make sure you have Python installed (3.x recommended) and install the dependencies:
```bash
pip install wordcloud wikipedia pillow

▶️ How to Run
Navigate to the project_01 directory:

bash
Copy
Edit
cd project_01
Run the script:

bash
Copy
Edit
python wordcloud_program.py
The generated image will be saved in the same folder.

📂 Repository Structure
markdown
Copy
Edit
GFG-Projects/
│
├── README.md
├── geeksforgeeks_wordcloud.png
└── project_01/
    └── wordcloud_program.py

✨ Author
Created by Anjali Niranjan — learning Python and building fun projects.

pgsql
Copy
Edit

If you save this in your `gfg_projects` folder as `README.md` and push, it’ll show up beautifully on GitHub.  

Do you want me to also adjust the script so it **always saves the image automatically** in the repo folder when you run it? That way, the PNG stays updated.
