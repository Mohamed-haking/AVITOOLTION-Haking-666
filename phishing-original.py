import sqlite3
from flask import Flask, render_template, request, redirect, url_for

# إنشاء تطبيق Flask
app = Flask(__name__)

# إنشاء قاعدة البيانات
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    # إنشاء جدول الصفحات
    c.execute('''
        CREATE TABLE IF NOT EXISTS pages
        (id INTEGER PRIMARY KEY, title TEXT, content TEXT)
    ''')
    # إنشاء جدول المحتوى
    c.execute('''
        CREATE TABLE IF NOT EXISTS content
        (id INTEGER PRIMARY KEY, page_id INTEGER, type TEXT, value TEXT)
    ''')
    conn.commit()
    conn.close()

# صفحة رئيسية
@app.route('/')
def index():
    return render_template('index.html')

# صفحة إنشاء صفحة جديدة
@app.route('/create-page', methods=['GET', 'POST'])
def create_page():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        # إدخال صفحة جديدة في قاعدة البيانات
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('INSERT INTO pages (title, content) VALUES (?, ?)', (title, content))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('create-page.html')

# صفحة إنشاء محتوى جديد
@app.route('/create-content', methods=['GET', 'POST'])
def create_content():
    if request.method == 'POST':
        page_id = request.form['page_id']
        type = request.form['type']
        value = request.form['value']
        # إدخال محتوى جديد في قاعدة البيانات
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('INSERT INTO content (page_id, type, value) VALUES (?, ?, ?)', (page_id, type, value))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('create-content.html')

# صفحة لعرض جميع الصفحات
@app.route('/pages')
def pages():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM pages')
    pages = c.fetchall()
    conn.close()
    return render_template('pages.html', pages=pages)

# صفحة لعرض محتوى صفحة معينة
@app.route('/page/<int:page_id>')
def page(page_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM pages WHERE id=?', (page_id,))
    page = c.fetchone()
    c.execute('SELECT * FROM content WHERE page_id=?', (page_id,))
    content = c.fetchall()
    conn.close()
    return render_template('page.html', page=page, content=content)

# تشغيل التطبيق
if __name__ == '__main__':
    init_db()  # تهيئة قاعدة البيانات عند بدء التشغيل
    app.run(debug=True)
