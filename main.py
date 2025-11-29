def build_roster(registrations):
    roster = {}  # course_id -> set of student_ids

    # Step 1: Build dictionary of sets to remove duplicates
    for student_id, course_id in registrations:
        if course_id not in roster:
            roster[course_id] = set()
        roster[course_id].add(student_id)

    # Step 2: Convert each set into a sorted list
    final_roster = {}
    for course_id, student_set in roster.items():
        final_roster[course_id] = sorted(student_set)

    return final_roster
