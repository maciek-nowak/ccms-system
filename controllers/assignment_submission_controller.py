from models.assignment_submission_model import AssignmentSubmission
from views.assignment_submission_view import *


def start_controller(assignment_submission):
    print_what_to_do()
    num = get_number()
    if num == '1':
        print_submission(assignment_submission)
