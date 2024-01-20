CLASS_NAMES = (
    ('NO_CLASS', 'No Class Selected'),
    ('BCA1A', 'BCA I Year (Section A)'),
    ('BCA1B', 'BCA I Year (Section B)'),
    ('BCA2', 'BCA II Year'),
    ('BCA3', 'BCA Final Year'),
    ('BSC1', 'BSC I Year'),
    ('BSC2', 'BSC II Year'),
    ('BSC3', 'BSC Final Year'),
    ('MSC1', 'MSC I Year'),
    ('MSC2', 'MSC Final Year'),
)

BCA_I_YEAR = (
    # Odd Semester papers
    # ('Computer Fundamentals', 'Computer Fundamentals'),
    # ('C Programming', 'C Programming'),
    # ('Statistical Methods', 'Statistical Methods'),
    # ('Discrete Mathematics - I', 'Discrete Mathematics - I'),
    # ('Operating Systems', 'Operating Systems'),
    # ('Office Automation', 'Office Automation'),

    # Even Semester papers
    ('Programming In C++', 'Programming In C++'),
    ('System Analysis and Design', 'System Analysis and Design'),
    ('Numerical Methods', 'Numerical Methods'),
    ('Discrete Mathematics - II', 'Discrete Mathematics - II'),
    ('Linux Operating System', 'Linux Operating System'),
    ('E-Commerce', 'E-Commerce'),

    ('Practical I', 'Practical I'),
    ('Practical II', 'Practical II'),
    ('Practical III', 'Practical III'),

    ('English', 'English'),
    ('Hindi', 'Hindi'),
)

BCA_II_YEAR = (
    # Odd Semester papers
    # ('Visual Basic Programming', 'Visual Basic Programming'),
    # ('Data Base Management System', 'Data Base Management System'),
    # ('Data Structures', 'Data Structures'),
    # ('Operations Research - I', 'Operations Research - I'),
    # ('Web Technology - I', 'Web Technology - I'),
    # ('Digital Electronics - I', 'Digital Electronics - I'),

    # Even Semester papers
    ('Software Engineering - I', 'Software Engineering - I'),
    ('SQL and PL/SQL', 'SQL and PL/SQL'),
    ('Theory of Computation', 'Theory of Computation'),
    ('Operations Research - II', 'Operations Research - II'),
    ('Web Technology - II', 'Web Technology - II'),
    ('Digital Electronics - II', 'Digital Electronics - II'),

    ('Practical I', 'Practical I'),
    ('Practical II', 'Practical II'),
    ('Practical III', 'Practical III'),
)

BCA_FINAL_YEAR = (
    # Odd Semester papers
    # ('Computer Graphics - I', 'Computer Graphics - I'),
    # ('Compiler Construction', 'Compiler Construction'),
    # ('VB.Net', 'VB.Net'),
    # ('Software Engineering - II', 'Software Engineering - II'),
    # ('PHP - I', 'PHP - I'),
    # ('Data Communication and Network - I', 'Data Communication and Network - I'),

    # Even Semester papers
    ('Computer Graphics - II', 'Computer Graphics - II'),
    ('Programming in Java', 'Programming in Java'),
    ('ASP.Net', 'ASP.Net'),
    ('Software Testing', 'Software Testing'),
    ('PHP - II', 'PHP - II'),
    ('Data Communication and Network - II', 'Data Communication and Network - II'),

    ('Practical I', 'Practical I'),
    ('Practical II', 'Practical II'),
    ('Practical III', 'Practical III'),
)

BSC_I_YEAR = (
    # Odd Semester papers
    # ('Programming in C', 'Programming in C'),
    # ('Fundamentals of IT', 'Fundamentals of IT'),

    # Even Semester papers
    ('Programming In C++', 'Programming In C++'),
    ('System Analysis and Design', 'System Analysis and Design'),
)

BSC_II_YEAR = (
    # Odd Semester papers
    # ('Data Structures', 'Data Structures'),
    # ('Operating Systems', 'Operating Systems'),

    # Even Semester papers
    ('Java Programming', 'Java Programming'),
    ('Linux Operating System', 'Linux Operating System'),
)

BSC_FINAL_YEAR = (
    # Odd Semester papers
    # ('Visual Basic Programming', 'Visual Basic Programming'),
    # ('Database Management System', 'Database Management System'),

    # Even Semester papers
    ('Compiler Construction', 'Compiler Construction'),
    ('SQL AND PL/SQL', 'SQL AND PL/SQL'),
)

MSC_I_YEAR = (
    # Odd Semester papers
    # ('Artificial Intelligence', 'Artificial Intelligence'),
    # ('Compiler Constructions', 'Compiler Construction'),
    # ('Discrete Mathematics', 'Discrete Mathematics'),
    # ('Research Methodology', 'Research Methodology'),

    # Even Semester papers
    ('Cloud Computing', 'Cloud Computing'),
    ('Machine Learning', 'Machine Learning'),
    ('MOOC Course', 'MOOC Course'),
    ('Apprenticeship/Mini Project', 'Apprenticeship/Mini Project'),
    ('Practical I', 'Practical I'),
    ('Practical II', 'Practical II'),
)

MSC_FINAL_YEAR = (
    # Odd Semester papers
    # ('Advanced Software Engineering', 'Advanced Software Engineering'),
    # ('Network Security', 'Network Security'),
    # ('Digital Image Processing', 'Digital Image Processing'),
    # ('MOOC Course', 'MOOC Course'),
    # ('Research Project/Dissertation', 'Research Project/Dissertation'),
    # ('Practical', 'Practical'),

    # Even Semester papers
    ('Big Data Analytics', 'Big Data Analytics'),
    ('Computer Vision', 'Computer Vision'),
    ('Deep Learning', 'Deep Learning'),
    ('Design and Analysis of Algorithm', 'Design and Analysis of Algorithm'),
    ('Research Project/Dissertation', 'Research Project/Dissertation'),
)


def get_class(tmp_cls):
    '''
    Check if given string is matched with classes ID
    '''
    if not tmp_cls:
        tmp_cls = ''

    tmp_cls = tmp_cls.upper()
    if any(class_id == tmp_cls for class_id, _ in CLASS_NAMES):
        return tmp_cls
    return 'NO_CLASS'


def get_subjects(class_name):
    if class_name in ('BCA1A', 'BCA1B'):
        return BCA_I_YEAR
    elif class_name == 'BCA2':
        return BCA_II_YEAR
    elif class_name == 'BCA3':
        return BCA_FINAL_YEAR
    elif class_name == 'BSC1':
        return BSC_I_YEAR
    elif class_name == 'BSC2':
        return BSC_II_YEAR
    elif class_name == 'BSC3':
        return BSC_FINAL_YEAR
    elif class_name == 'MSC1':
        return MSC_I_YEAR
    elif class_name == 'MSC2':
        return MSC_FINAL_YEAR
    else:
        return []
