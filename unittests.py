from handleFiles import *
import pytest

class_instance=HandleFiles()

fileId=None

def setup_module(module):
    global fileId
    fileId=class_instance.createFileWithText("nombre test archivo con palabra","descripcion de prueba","mensaje para testear")[0]

def teardown_module(module):
    class_instance.deleteFile(fileId)

def test_seCreaArchivo():
    fileIdArchivo,response=class_instance.createFile("nombre test archivo","descripcion x")
    assert(response)
    class_instance.deleteFile(fileIdArchivo)

def test_archivoContienePalabra():
    response=class_instance.searchWord(fileId,"mensaje")
    assert (response)

def test_archivoNoContienePalabra():
    response=class_instance.searchWord(fileId,"palabra x")
    assert not (response)

def test_archivoExiste():
    response = class_instance.fileExists(fileId)
    assert (response)

def test_archivoNoExiste():
    response = class_instance.fileExists('a')
    assert not (response)

