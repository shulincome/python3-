import sys
script, input_encoding, error = sys.argv


#定义主函数
def main(language_file, encoding, errors):
        #对文件进行按行读取readline()
    line = language_file.readline()  
    #如果这行没有内容，进行下一行的读取
    if line:
        print_line(line, encoding, errors)
        return main(language_file,encoding, errors)

#
def print_line(line, encoding, errors):
    next_lang = line.strip()  #获取当前行数
    raw_bytes = next_lang.encode(encoding, errors=errors)  # Unicode编码
    cooked_string = raw_bytes.decode(encoding, errors=errors)#Unicode 解码

    print(raw_bytes, "<===>", cooked_string)

#对参数luanguages进行赋值，打开文本文件
languages = open("languages.txt",encoding="utf-8")
#运行主函数
main(languages, input_encoding, error)