def is_equal_string(utf8_string, utf16_string):
   if isinstance(utf8_string, bytes):
       utf8_string = utf8_string.decode('utf-8')
       if isinstance(utf16_string, bytes):
           utf16_string = utf16_string.decode('utf-16')
           return utf8_string == utf16_string