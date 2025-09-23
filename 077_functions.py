def percent(marks):
    p = ((marks[0] + marks[1] + marks[2] + marks[3]) / 400) * 100
    return p

marks = [45, 78, 86, 77]
# percentage = (sum(marks) / 400) * 100
# percentage = ((marks[0] + marks[1] + marks[2] + marks[3]) / 400) * 100
percentage = percent(marks)

marks1 = [45, 98, 86, 72]
# percentage1 = (sum(marks1) / 400) * 100
# percentage1 = ((marks1[0] + marks1[1] + marks1[2] + marks1[3]) / 400) * 100
percentage1 = percent(marks1)
print(percentage, percentage1)