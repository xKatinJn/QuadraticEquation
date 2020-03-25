from flask import jsonify, request

from SOLUTION_3_BONUS.app.api import bp
from SOLUTION_3_BONUS.app.scripts.QudraticSolver import QuadraticEquation


@bp.route('/solve', methods=['GET'])
def solve():

    response = {'solve': None,
                'status_code': 200
                }
    a = request.args.get('a')
    b = request.args.get('b')
    c = request.args.get('c')
    try:
        solver = QuadraticEquation(a, b, c)
        solver = solver.get_solution()
    except ValueError as error:
        response['error'] = str(error) + '; Incorrect Values'
        return jsonify(response)
    except TypeError as error:
        response['error'] = str(error) + '; Missed values'
        return jsonify(response)
    if type(solver) == bool:
        response['solve'] = 'No valid radicals'
    else:
        response['solve'] = f'X1={solver[0]} X2={solver[1]}'

    return jsonify(response)
