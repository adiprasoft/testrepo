#include <Array.au3>
#include <File.au3>

$parentFolder = @ScriptDir
MsgBox(0,0,$parentFolder)

$array = _FileListToArray($parentFolder,Default,Default,True)

_ArrayDisplay($array)

Global $fhandle = FileOpen("log.txt", 1)
Func logfile($data)
	$fhangle = FileWrite("log.txt", $data & @CRLF )
EndFunc


Func subfloders($parentFolder)
	$array = _FileListToArrayRec($parentFolder,Default,$FLTAR_FILESFOLDERS,$FLTAR_RECUR,'', $FLTAR_FULLPATH)
	for $x=1 to $array[0]
		;MsgBox(0,0,$array[$x])
		If IsDir($array[$x]) Then
			logfile('This is a directory '& $array[$x])
			;subfloders($array[$x])
			;MsgBox(0,'File Attribute' ,'This is a directory ' & $array[$x])
		Else
			;MsgBox(0,'Files','This is a file ' & $array[$x])
			logfile('This is a File' & $array[$x])
		EndIf
	Next
EndFunc

subfloders($parentFolder)

Func IsDir($sFilePath)
    Return StringInStr(FileGetAttrib($sFilePath), "D") > 0
EndFunc
