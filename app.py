from flask import Flask, render_template, request, send_file
import instaloader
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    loader = instaloader.Instaloader()
    post = instaloader.Post.from_shortcode(loader.context, url.split('/')[-2])

    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    
    filepath = f'downloads/{post.shortcode}.jpg'
    loader.download_pic(filepath, post.url, post.date_utc)
    
    return send_file(filepath, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
