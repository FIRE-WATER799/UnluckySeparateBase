import io
import os

import PyPDF2
from flask import Flask, send_file, send_from_directory

app = Flask(__name__)


@app.route('/USHistory/<chapter>/', defaults={'section': None})
@app.route('/USHistory/<chapter>/<section>')
def get_book(chapter, section):
    pdf_path = os.path.join('books',
                            "ch" + "{:02d}".format(int(chapter)) + ".pdf")
    if section != None:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            sections = {
                5: {
                    1: [4, 13],
                    2: [14, 18],
                    3: [19, 23]
                },
                6: {
                    1: [4, 7],
                    2: [8, 12],
                    3: [13, 21]
                },
                7: {
                    1: [4, 9],
                    2: [10, 14],
                    3: [15, 19]
                },
                8: {
                    1: [4, 9],
                    2: [10, 13],
                    3: [14, 17],
                    4: [18, 23]
                },
                9: {
                    1: [4, 10],
                    2: [11, 14],
                    3: [15, 23],
                    4: [23, 27],
                    5: [28, 33]
                },
                10: {
                    1: [4, 7],
                    2: [8, 13],
                    3: [14, 20],
                    4: [21, 27]
                },
                11: {
                    1: [4, 12],
                    2: [13, 19],
                    3: [20, 27],
                    4: [28, 33]
                },
                12: {
                    1: [4, 10],
                    2: [11, 13],
                    3: [14, 19],
                },
                13: {
                    1: [4, 9],
                    2: [10, 13],
                    3: [14, 19],
                    4: [20, 25]
                },
                14: {
                    1: [4, 11],
                    2: [12, 17],
                    3: [18, 23]
                },
                15: {
                    1: [4, 10],
                    2: [11, 17],
                    3: [18, 23],
                    4: [24, 28],
                    5: [29, 33]
                },
                16: {
                    1: [4, 11],
                    2: [12, 17],
                    3: [18, 25],
                    4: [26, 33]
                },
                17: {
                    1: [4, 10],
                    2: [11, 19],
                    3: [20, 29],
                    4: [30, 35]
                },
                18: {
                    1: [4, 10],
                    2: [11, 17],
                    3: [18, 23],
                    4: [24, 29]
                },
                19: {
                    1: [4, 10],
                    2: [11, 19],
                    3: [20, 25],
                    4: [26, 29]
                },
                20: {
                    1: [4, 12],
                    2: [13, 17],
                    3: [18, 25]
                },
                21: {
                    1: [4, 11],
                    2: [12, 18],
                    3: [19, 25]
                },
                22: {
                    1: [4, 9],
                    2: [10, 15],
                    3: [16, 21],
                    4: [22, 27],
                    5: [28, 35]
                },
                23: {
                    1: [4, 9],
                    2: [10, 14],
                    3: [15, 19]
                },
                24: {
                    1: [4, 11],
                    2: [12, 17],
                    3: [18, 25],
                    4: [26, 31]
                },
                25: {
                    1: [4, 7],
                    2: [8, 12],
                    3: [13, 19],
                    4: [20, 27]
                }
            }
            try:
                pages = [
                    pdf_reader.pages[i]
                    for i in range(sections[int(chapter)][int(section)][0] -
                                   1, sections[int(chapter)][int(section)][1])
                ]
            except KeyError:
                return "Invalid chapter or section", 404
            pdf_writer = PyPDF2.PdfWriter()
            for page in pages:
                pdf_writer.add_page(page)

            buffer = io.BytesIO()
            pdf_writer.write(buffer)
            # Set the desired filename
            buffer.seek(0)
            filename = "ch" + "{:02d}".format(
                int(chapter)) + "sec" + "{:02d}".format(int(section)) + ".pdf"
            # Return the BytesIO object as a file download
            return send_file(buffer,
                             mimetype='application/pdf',
                             as_attachment=True,
                             download_name=filename)
    else:
        return send_from_directory(
            'books', "ch" + "{:02d}".format(int(chapter)) + ".pdf")


@app.route('/USHistory')
def USHistory():
    merger = PyPDF2.PdfWriter()

    for i in os.listdir("books"):
        h = open("books/" + i, "rb")
        merger.append(fileobj=h)
    buffer = io.BytesIO()
    merger.write(buffer)
    # Set the desired filename
    buffer.seek(0)
    filename = "USHistory.pdf"
    # Return the BytesIO object as a file download
    return send_file(buffer,
                     mimetype='application/pdf',
                     as_attachment=True,
                     download_name=filename)


if __name__ == '__main__':
    app.run(debug=True)
