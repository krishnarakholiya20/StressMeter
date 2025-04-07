class AcademicStress:
    def assignment_deadlines(self, pending_count):
        return f"{'Overloaded' if pending_count > 3 else 'Manageable'} assignments"

    def exam_pressure(self, upcoming_exams):
        return f"{'High' if upcoming_exams > 2 else 'Low'} exam pressure"

    def study_hours(self, hours):
        return f"{'Excessive' if hours > 6 else 'Balanced'} study time"

    def academic_performance(self, grade_score):
        return f"{'Poor' if grade_score < 60 else 'Good'} academic performance"

    def peer_competition(self, peer_score):
        return f"{'High' if peer_score > 7 else 'Normal'} peer competition"

    def teacher_expectations(self, pressure_level):
        return f"{'Stressful' if pressure_level > 7 else 'Supportive'} teacher expectations"

    def course_difficulty(self, difficulty_score):
        return f"{'Difficult' if difficulty_score > 7 else 'Moderate'} course level"

    def feedback_quality(self, feedback_score):
        return f"{'Low' if feedback_score < 4 else 'Helpful'} feedback"

    def workload_balance(self, workload_score):
        return f"{'Unbalanced' if workload_score < 4 else 'Balanced'} workload"

    def class_participation(self, participation_level):
        return f"{'Low' if participation_level < 3 else 'Active'} class participation"
