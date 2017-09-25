# coding=utf-8
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        try:
            fout = open('output.html','w')
            print "文件打开"

            fout.write("<html>")
            fout.write("<head><meta charset='utf-8'></head>")
            fout.write("<body>")
            fout.write("<table>")
            # ascii
            for data in self.datas:
                fout.write("<tr>")
                fout.write("<td>%s</td>" % data['url'])
                fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
                fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
                fout.write("</tr>")

            fout.write("</table>")
            fout.write("</body>")
            fout.write("</html>")
        except:
            print "写入失败"
        else:
            print "写入成功"
        finally:
            fout.close()
            print "文件关闭"
