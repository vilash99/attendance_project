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
    ('DSC-I: Mathematics Foundation to CS', 'DSC-I: Mathematics Foundation to CS'),
    ('DSC-II: Basics of Computer Architecture', 'DSC-II: Basics of Computer Architecture'),
    ('SEC: Problem Solving Techniques with C', 'SEC: Problem Solving Techniques with C'),
    ('AEC: English Compulsory', 'AEC: English Compulsory'),
    ('VEC: Environmental Science', 'VEC: Environmental Science'),
    ('IKS: Vedic Mathematics', 'IKS: Vedic Mathematics'),
    ('SEC: Practical I', 'SEC: Practical I'),
    ('DSC-II: Practical II', 'DSC-II: Practical II'),
)

BCA_I_EVEN = (
    ('DSC-I: Programming in C++', 'DSC-I: Programming in C++'),
    ('DSC-II: Database Management System', 'DSC-II: Database Management System'),
    ('SEC-I: Data Structures', 'SEC-I: Data Structures'),
    ('DSC-III: Operating System and Linux', 'DSC-III: Operating System and Linux'),
    ('SEC-II: Web Technologies', 'SEC-II: Web Technologies'),
    ('VEC: Constitution of India', 'VEC: Constitution of India'),
    ('DSC-I: Practical I', 'DSC-I: Practical I'),
    ('SEC-I: Practical II', 'SEC-I: Practical II'),
    ('SEC-II: Practical III', 'SEC-II: Practical III'),
)


BCA_II_ODD = (
    ('DSC-I: Object Oriented Programming using JAVA', 'DSC-I: Object Oriented Programming using JAVA'),
    ('DSC-II: Probability and Statistics', 'DSC-II: Probability and Statistics'),
    ('SEC-I: Python Programming', 'SEC-I: Python Programming'),
    ('DSC-III: Software Engineering', 'DSC-III: Software Engineering'),
    ('DSC-IV: Basics of Data Analytics using Spreadsheet', 'DSC-IV: Basics of Data Analytics using Spreadsheet'),
    ('SEC-II: Practical SQL and PL/SQL', 'SEC-II: Practical SQL and PL/SQL'),
    ('DSC-I: Practical I', 'DSC-I: Practical I'),
    ('SEC-I: Practical II', 'SEC-I: Practical II'),
    ('DSC-IV: Practical III', 'DSC-IV: Practical III'),
)

BCA_II_EVEN = (
    ('DSC-I: Artificial Intelligence', 'DSC-I: Artificial Intelligence'),
    ('DSC-II: Computer Networks', 'DSC-II: Computer Networks'),
    ('DSC-III: PHP', 'DSC-III: PHP'),
    ('DSC-IV: Design and Analysis of Algorithm', 'DSC-IV: Design and Analysis of Algorithm'),
    ('SEC-I: Data Visualization', 'SEC-I: Data Visualization'),
    ('VAC: Design Thinking and Innovation', 'VAC: Design Thinking and Innovation'),
    ('DSC-I: Practical I', 'DSC-I: Practical I'),
    ('DSC-III: Practical II', 'DSC-III: Practical II'),
    ('SEC-I: Practical III', 'SEC-I: Practical III'),
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
    ('Linux Operating Systems', 'Linux Operating Systems'),
    ('Practical', 'Practical'),
)

BSC_II_EVEN = (
    ('Java Programming', 'Java Programming'),
    ('Software Engineering', 'Software Engineering'),
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
    ('R Programming', 'R Programming'),
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
    ('Cyber Forensics', 'Cyber Forensics'),
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


CLASS_SUBJECT_CONFIG = {
    # BCA
    'BCA1A': ('BCA_I',      BCA_I_EVEN,      BCA_I_ODD),
    'BCA1B': ('BCA_I',      BCA_I_EVEN,      BCA_I_ODD),
    'BCA2':  ('BCA_II',     BCA_II_EVEN,     BCA_II_ODD),
    'BCA3':  ('BCA_III',    BCA_FINAL_EVEN,  BCA_FINAL_ODD),

    # BSC
    'BSC1':  ('BSC_I',      BSC_I_EVEN,      BSC_I_ODD),
    'BSC2':  ('BSC_II',     BSC_II_EVEN,     BSC_II_ODD),
    'BSC3':  ('BSC_III',    BSC_FINAL_EVEN,  BSC_FINAL_ODD),

    # MSC
    'MSC1':  ('MSC_I',      MSC_I_EVEN,      MSC_I_ODD),
    'MSC2':  ('MSC_II',     MSC_FINAL_EVEN,  MSC_FINAL_ODD),
}

def get_subjects(class_name: str):
    """
    Return subject choices for given class_name
    based on whether current semester is odd or even.

    Env vars:
      - flag_name from CLASS_SUBJECT_CONFIG (e.g. 'BCA_I')
        True  => ODD
        False => EVEN
    """
    cfg = CLASS_SUBJECT_CONFIG.get(class_name)
    if not cfg:
        return []

    flag_name, even_subjects, odd_subjects = cfg
    is_odd_semester = config(flag_name, cast=bool)

    return odd_subjects if is_odd_semester else even_subjects
