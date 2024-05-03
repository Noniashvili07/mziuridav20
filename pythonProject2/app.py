from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# List of dictionaries for storing books
books = [
    {"id": 1, "title": "Eleven minutes", "author": "Paulho Coelho", "year": 2003},
    {"id": 2, "title": "1984", "author": "George Orwell", "year": 1949},
    {"id": 3, "title": "Crime and punichment", "author": "Fydor Dostoevsky", "year": 1866}
]

# Base HTML file
@app.route('/')
def home():
    return render_template('index.html', books=books)

@app.route('/book/<int:book_id>')
def book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return render_template('book.html', book=book)
@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        new_book = {
            "id": len(books) + 1,
            "title": request.form['title'],
            "author": request.form['author'],
            "year": int(request.form['year'])
        }
        books.append(new_book)
        return redirect(url_for('home'))
    return render_template('add_book.html')

if __name__ == '__main__':
    app.run(debug=True)
