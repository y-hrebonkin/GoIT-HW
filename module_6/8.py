def save_applicant_data(source, output):
    with open(output, 'w') as f:
        for applicant in source:
            name = applicant['name']
            specialty = applicant['specialty']
            math = applicant['math']
            lang = applicant['lang']
            eng = applicant['eng']
            f.write(f"{name},{specialty},{math},{lang},{eng}\n")