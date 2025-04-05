import datetime

from fillpdf import fillpdfs

form_fields = fillpdfs.get_form_fields(r"PDfPath")

for key,value in form_fields.items():
    if value != '':
        print(key,value)

data_dict = {
    '50' : "hello, Man, howare, you",
    'birth_mm' : 88,
    'birth_dd' : 88,
    'sex' : 'M',
    'cpt1': 'XXXXX',
    'cpt2': 'XXXXX',
    'cpt3': 'xxxxx',
    'cpt4': 'xxxxx',
    'cpt5': 'xxxxx',
    'cpt6': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
}

# print(data_dict)

fillpdfs.write_fillable_pdf(input_pdf_path=r'pdfpath', output_pdf_path='new_filled_form.pdf', data_dict=data_dict)