'''
Python 中 r 的用法主要有兩種：在字串前加 r 作為 「原始字串」，
  用於取消轉義符（例如在處理檔案路徑時），
以及在 str.format() 函式中使用 !r,表示使用 repr()
  函數來格式化字串。 
r 作為原始字串前綴
  作用：在字串前加上 r,可以防止反斜線 \ 被解釋為轉義字符。
  應用：這對於處理包含大量反斜線的字串特別有用，例如 Windows 檔案路徑。
範例：
  print(r"C:\new\nfile") 會印出 C:\new\nfile。
  print("C:\new\nfile") 會印出 C:\new 加上一個換行，然後是 file。 
!r 作為 str.format() 的格式化指令
  作用：在 str.format() 中，!r 是一個格式化指令，它會對傳入的物件呼叫 repr() 函數，而不是 str() 函數。
  應用：這會將物件轉換成 Python 解釋器可以理解的表示形式，通常會在字串前後加上引號。
範例：
print("{!r}".format("hello")) 會印出 'hello'。
print("{}".format("hello")) 會印出 hello。 
總結
  符號 	 說明
  r	    在字串前加上 r,表示此字串為「原始字串」,取消轉義字符的處理。
  !r	在 str.format() 中，表示使用 repr() 函數來格式化字串。
'''
print("{!r}".format("hello")) #會印出 'hello'。
print("{}".format("hello")) #會印出 hello。 