Hello All,
I was having a use case where I need to programatically fill CPT code to CMS-1500 pdf form.

I worte a simple python script to ease up the process in which I am using `fillpdf` library to fill up pdf form.

Steps to run.

1. pip install fillpdf
2. provide your pdf form path to `fillpdfs.get_form_fields` method.
3. create a data_dict to store all changes with the desired key extracted from your form.
4. pass all your input to `fillpdfs.write_fillable_pdf` method
5. run your python script.

Note:- I am using this script to fill CMS-1500 pdf form but this script can be modified to fill out any pdf form accordingly.
