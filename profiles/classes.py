CLASS_NAMES = [
    ('NO_CLASS', 'No Class Selected'),
    ('BCA1A', 'BCA I Year (Section A)'),
    ('BCA1B', 'BCA I Year (Section B)'),
    ('BCA2', 'BCA II Year'),
    ('BCA3', 'BCA Final Year'),
    ('BSC1', 'BSC I Year'),
    ('BSC2', 'BSC II Year'),
    ('BSC3', 'BSC Final Year'),
]

BCA_I_YEAR = [
    ('Computer Fundamentals', 'Computer Fundamentals'),
    ('C Programming', 'C Programming'),
    ('Statistical Methods', 'Statistical Methods'),
    ('Discrete Mathematics - I', 'Discrete Mathematics - I'),
    ('Operating Systems', 'Operating Systems'),
    ('Office Automation', 'Office Automation'),
    ('Practical I', 'Practical I'),
    ('Practical II', 'Practical II'),
    ('Practical III', 'Practical III'),

    # Even Semester papers
    # ('Programming In C++', 'Programming In C++'),
    # ('System Analysis and Design', 'System Analysis and Design'),
    # ('Numerical Methods', 'Numerical Methods'),
    # ('Discrete Mathematics - II', 'Discrete Mathematics - II'),
    # ('Linux Operating System', 'Linux Operating System'),
    # ('E-Commerce', 'E-Commerce'),

    ('English', 'English'),
    ('Hindi', 'Hindi'),
]

BCA_II_YEAR = [
    ('Visual Basic Programming', 'Visual Basic Programming'),
    ('Data Base Management System', 'Data Base Management System'),
    ('Data Structures', 'Data Structures'),
    ('Operations Research - I', 'Operations Research - I'),
    ('Web Technology - I', 'Web Technology - I'),
    ('Digital Electronics - I', 'Digital Electronics - I'),

    # Even Semester papers
    # ('Software Engineering - I', 'Software Engineering - I'),
    # ('SQL and PL/SQL', 'SQL and PL/SQL'),
    # ('Theory of Computation', 'Theory of Computation'),
    # ('Operations Research - II', 'Operations Research - II'),
    # ('Web Technology - II', 'Web Technology - II'),
    # ('Digital Electronics - II', 'Digital Electronics - II'),

    ('Practical I', 'Practical I'),
    ('Practical II', 'Practical II'),
    ('Practical III', 'Practical III'),
]

BCA_FINAL_YEAR = [
    ('Computer Graphics - I', 'Computer Graphics - I'),
    ('Compiler Construction', 'Compiler Construction'),
    ('VB.Net', 'VB.Net'),
    ('Software Engineering - II', 'Software Engineering - II'),
    ('PHP - I', 'PHP - I'),
    ('Data Communication and Network - I', 'Data Communication and Network - I'),

    # Even Semester papers
    # ('Computer Graphics - II', 'Computer Graphics - II'),
    # ('Programming in Java', 'Programming in Java'),
    # ('ASP.Net', 'ASP.Net'),
    # ('Software Testing', 'Software Testing'),
    # ('PHP - II', 'PHP - II'),
    # ('Data Communication and Network - II', 'Data Communication and Network - II'),

    ('Practical I', 'Practical I'),
    ('Practical II', 'Practical II'),
    ('Practical III', 'Practical III'),
]

BSC_I_YEAR = [
    ('Programming in C', 'Programming in C'),
    ('Fundamentals of IT', 'Fundamentals of IT'),

    # Even Semester papers
    # ('Programming In C++', 'Programming In C++'),
    # ('System Analysis and Design', 'System Analysis and Design'),
]

BSC_II_YEAR = [
    ('Data Structures', 'Data Structures'),
    ('Operating Systems', 'Operating Systems'),

    # Even Semester papers
    # ('Java Programming', 'Java Programming'),
    # ('Linux Operating System', 'Linux Operating System'),
]

BSC_FINAL_YEAR = [
    ('Visual Basic Programming', 'Visual Basic Programming'),
    ('Database Management System', 'Database Management System'),

    # Even Semester papers
    # ('Compiler Construction', 'Compiler Construction'),
    # ('SQL AND PL/SQL', 'SQL AND PL/SQL'),
]


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
    else:
        return []
