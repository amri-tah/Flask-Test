from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [
    {'id': 1, 
     'title' : "Data Analyst",
     'location': "Coimbatore, India",
     'salary': "Rs. 1,00,000"
    },

    {'id': 2, 
     'title' : "Data Scientist",
     'location': "Bengaluru, India",
     'salary': "Rs. 1,50,000"
    },

    {'id': 3, 
     'title' : "Full Stack Developer",
     'location': "Remote",
     'salary': "Rs. 1,50,000"
    },

    {'id': 4, 
     'title' : "Back Stack Developer",
     'location': "San Francisco, USA",
     'salary': "$12000"
    },
]

@app.route("/")
def hello():
    return render_template('home.html', 
                           jobs=jobs)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(jobs)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)