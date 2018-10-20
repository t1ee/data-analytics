Sub TotalStock()

Dim Sym As String
Dim Vol As Double
Vol = 0

lastrow = Cells(Rows.Count, 1).End(xlUp).Row
Summary_Table_Row = 2

For i = 2 To lastrow
   If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
   Sym = Cells(i, 1).Value
   Vol = Vol + Cells(i, 7).Value
   Range("I" & Summary_Table_Row).Value = Sym
   Range("J" & Summary_Table_Row).Value = Vol
   
   Summary_Table_Row = Summary_Table_Row + 1
   
   Vol = 0
   
   Else
   Vol = Vol + Cells(i, 7).Value
   End If
   Next i

End Sub