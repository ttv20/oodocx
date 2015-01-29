from oodocx import oodocx

d = oodocx.Docx()
body = d.get_body()
body.append(oodocx.paragraph('Hello World!'))
d.save('Example1.docx')

d = oodocx.Docx()
body = d.get_body()
body.append(oodocx.paragraph('Hello World!'))

table_info = []
table_info.append(["test1", "test2"])
table_info.append(["test3", "test4"])
table_info.append(["test5", "test6"])
table_info.append(["test7", "test8"])

body.append(oodocx.table(contents=table_info,
                         heading=False,
                         colw=[3348, 6228],
                         borders={"all": {"color": "#000000", "sz": "4",
                                  "val": "single"}},
                         celstyle=[{"align": u"left"}, {"align": u"center"}]))

d.save('ExampleTable.docx')
