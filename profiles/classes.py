from decouple import config

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

BCA_I_ODD = (
    ('Computer Fundamentals', 'Computer Fundamentals'),
    ('C Programming', 'C Programming'),
    ('Statistical Methods', 'Statistical Methods'),
    ('Discrete Mathematics - I', 'Discrete Mathematics - I'),
    ('Operating Systems', 'Operating Systems'),
    ('Office Automation', 'Office Automation'),
    ('Practical I', 'Practical I'),
    ('Practical II', 'Practical II'),
    ('Practical III', 'Practical III'),
    ('English', 'English'),
    ('Hindi', 'Hindi'),
)

BCA_I_EVEN = (
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

BCA_II_ODD = (
    ('Visual Basic Programming', 'Visual Basic Programming'),
    ('Data Base Management System', 'Data Base Management System'),
    ('Data Structures', 'Data Structures'),
    ('Operations Research - I', 'Operations Research - I'),
    ('Web Technology - I', 'Web Technology - I'),
    ('Digital Electronics - I', 'Digital Electronics - I'),
    ('Practical I', 'Practical I'),
    ('Practical II', 'Practical II'),
    ('Practical III', 'Practical III'),
)

BCA_II_EVEN = (
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

BCA_FINAL_ODD = (
    ('Computer Graphics - I', 'Computer Graphics - I'),
    ('Compiler Construction', 'Compiler Construction'),
    ('VB.Net', 'VB.Net'),
    ('Software Engineering - II', 'Software Engineering - II'),
    ('PHP - I', 'PHP - I'),
    ('Data Communication and Network - I', 'Data Communication and Network - I'),
    ('Practical I', 'Practical I'),
    ('Practical II', 'Practical II'),
    ('Practical III', 'Practical III'),
)

BCA_FINAL_EVEN = (
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

BSC_I_ODD = (
    ('Programming in C', 'Programming in C'),
    ('Fundamentals of IT', 'Fundamentals of IT'),
    ('Practical', 'Practical'),
)

BSC_I_EVEN = (
    ('Programming In C++', 'Programming In C++'),
    ('System Analysis and Design', 'System Analysis and Design'),
    ('Practical', 'Practical'),
)

BSC_II_ODD = (
    ('Data Structures', 'Data Structures'),
    ('Operating Systems', 'Operating Systems'),
    ('Practical', 'Practical'),
)

BSC_II_EVEN = (
    ('Java Programming', 'Java Programming'),
    ('Linux Operating System', 'Linux Operating System'),
    ('Practical', 'Practical'),
)

BSC_FINAL_ODD = (
    ('Visual Basic Programming', 'Visual Basic Programming'),
    ('Database Management System', 'Database Management System'),
    ('Practical', 'Practical'),
)

BSC_FINAL_EVEN = (
    ('Compiler Construction', 'Compiler Construction'),
    ('SQL AND PL/SQL', 'SQL AND PL/SQL'),
    ('Practical', 'Practical'),
)


MSC_I_ODD = (
    ('Artificial Intelligence', 'Artificial Intelligence'),
    ('Compiler Constructions', 'Compiler Construction'),
    ('Discrete Mathematics', 'Discrete Mathematics'),
    ('Research Methodology', 'Research Methodology'),
    ('Practical I', 'Practical I'),
    ('Practical II', 'Practical II'),
)

MSC_I_EVEN = (
    ('Cloud Computing', 'Cloud Computing'),
    ('Machine Learning', 'Machine Learning'),
    ('MOOC Course', 'MOOC Course'),
    ('Apprenticeship/Mini Project', 'Apprenticeship/Mini Project'),
    ('Practical I', 'Practical I'),
    ('Practical II', 'Practical II'),
)

MSC_FINAL_ODD = (
    ('Advanced Software Engineering', 'Advanced Software Engineering'),
    ('Network Security', 'Network Security'),
    ('Digital Image Processing', 'Digital Image Processing'),
    ('Computer Graphics', 'Computer Graphics'),
    ('Research Project/Dissertation', 'Research Project/Dissertation'),
    ('Practical', 'Practical'),
)

MSC_FINAL_EVEN = (
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
    # 0 - EVEN, 1 - ODD
    semester = config('SEMESTER', cast=bool)

    if class_name in ('BCA1A', 'BCA1B'):
        return BCA_I_ODD if semester else BCA_I_EVEN
    elif class_name == 'BCA2':
        return BCA_II_ODD if semester else BCA_II_EVEN
    elif class_name == 'BCA3':
        return BCA_FINAL_ODD if semester else BCA_FINAL_EVEN
    elif class_name == 'BSC1':
        return BSC_I_ODD if semester else BSC_I_EVEN
    elif class_name == 'BSC2':
        return BSC_II_ODD if semester else BSC_II_EVEN
    elif class_name == 'BSC3':
        return BSC_FINAL_ODD if semester else BSC_FINAL_EVEN
    elif class_name == 'MSC1':
        return MSC_I_ODD if semester else MSC_I_EVEN
    elif class_name == 'MSC2':
        return MSC_FINAL_ODD if semester else MSC_FINAL_EVEN
    else:
        return []
