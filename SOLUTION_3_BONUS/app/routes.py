from flask import render_template, url_for

from SOLUTION_3_BONUS.app.forms import SolverForm
from SOLUTION_3_BONUS.app import app
from SOLUTION_3_BONUS.app.scripts.QuadraticSolver import QuadraticEquation


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Главная')


@app.route('/solver', methods=['GET', 'POST'])
def solver():
    form = SolverForm()
    solved = False
    radicals = None
    error = False

    print('First')
    if form.validate_on_submit():
        print('Second')
        a = form.a_value.data
        b = form.b_value.data
        c = form.c_value.data
        try:
            solve = QuadraticEquation(a, b, c)
            solve = solve.get_solution()
            if type(solve) == bool:
                solved = True
            else:
                radicals = solve
                solved = True
        except ValueError:
            error = True

        return render_template('solver.html', title='Решатель', form=form, solved=solved, radicals=radicals, error=error)
    return render_template('solver.html', title='Решатель', form=form, solved=solved, radicals=radicals, error=error)
