from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

def get_user_notes():
    # Get notes for the current user from session or initialize if not present
    return session.setdefault('notes', [])

@app.route('/', methods=["GET", "POST"])
def index():
    user_notes = get_user_notes()
    if request.method == "POST":
        note = request.form.get("note")
        if note:
            user_notes.append(note)
            session['notes'] = user_notes
            return redirect(url_for('index'))  
    return render_template("home.html", notes_with_index=enumerate(user_notes))

@app.route('/clear')
def clear():
    session.pop('notes', None)  # Clear notes for the current user
    return redirect(url_for('index')) 

if __name__ == '__main__':
    app.run(debug=True)