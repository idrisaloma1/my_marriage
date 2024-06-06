from flask import Flask, render_template, request

app = Flask(__name__)

class TooYoungException(Exception):
    def __init__(self, arg):
        self.msg = arg

class TooOldException(Exception):
    def __init__(self, arg):
        self.msg = arg

class JobSecureException(Exception):
    def __init__(self, arg):
        self.msg = arg

class IslamicReligionException(Exception):
    def __init__(self, arg):
        self.msg = arg

class PhysicalDesirabilityException(Exception):
    def __init__(self, arg):
        self.msg = arg

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        age = int(request.form['age'])
        if age > 40:
            raise TooOldException("With your age you need special attention...consult the counselling unit, dial +2348072889844 for more guidance")
        elif age < 18:
            raise TooYoungException("Please wait for a few more years, concentrate on your studies, get a suitable and a secure a job before setting up for marriage. Dial this WhatsApp +2348072889844 for more counselling.")
        else:
            job_secure = request.form['job_secure'].lower()
            if job_secure != 'yes':
                raise JobSecureException("Your job is not secure, and that may affect your marriage prospects. Try to secure a job and intensify your Prayer, HASBUNALLAHU WANE'EMAL WAKIL.")
            
            religion = request.form['religion'].strip()
            if religion.lower() != 'islam':
                raise IslamicReligionException("We are sorry, but our services are only available for those of the Islamic faith.")
            
            physical_desirability = request.form['physical_desirability'].lower()
            if physical_desirability != 'no':
                raise PhysicalDesirabilityException("Physical desirability is an important factor in finding a match. Take steps to improve your physical well-being. Dial +2348072889844 for more on health counselling.")
            else:
                return "You will get match details soon by email. Contact this number +2348072889844 on WhatsApp for more guidance."

    except (TooYoungException, TooOldException, JobSecureException, IslamicReligionException, PhysicalDesirabilityException) as e:
        return e.msg

if __name__ == '__main__':
    app.run(debug=True)
