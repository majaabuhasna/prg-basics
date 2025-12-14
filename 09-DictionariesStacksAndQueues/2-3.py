all_students = {"Alice", "John", "Sara", "Bob"}
attended_students = {"Alice", "Bob"}

absent_students = set(all_students - attended_students)  # Difference
print(absent_students)