import pytest
import file_encryption
from file_encryption import menu,load_keys,generate_keys,encrypt_file,decrypt_file
from unittest.mock import patch
import csv
from cryptography.fernet import Fernet

@pytest.fixture
def sample_csv(tmp_path):
    test_csv=tmp_path/"students.csv"
    with open(test_csv,"w",newline="") as test_file:
        writer=csv.DictWriter(test_file,fieldnames=["Students"])
        writer.writeheader()
        writer.writerow({"Students":"Mubarak"})
        writer.writerow({"Students":"Awwal"})
    return test_csv

@pytest.mark.parametrize("option,func_name",[
    (1,"encrypt_file"),
    (2,"decrypt_file"),
])

def test_menu_calls_function(option,func_name,sample_csv):
    
    with patch(f"file_encryption.{func_name}")as mock_func:
        inputs=[option,sample_csv,3]
        with patch("builtins.input",side_effect=inputs):
            menu()
    mock_func.assert_called_once()

def test_load_keys(tmp_path):
    test_csv=tmp_path/"secret.keys"
    file_encryption.filename=test_csv
    key=Fernet.generate_key()
    with open(test_csv,"wb") as key_load:
        key_load.write(key)
    result=load_keys()
    assert len(result)==len(key)
        
def test_generate_keys(tmp_path,capsys):
    test_csv=tmp_path/"secret.key"
    file_encryption.filename=test_csv
    generate_keys()
    with open(test_csv,"rb") as key_file:
        reader=key_file.read()
        rows=list(reader)
    
    captured=capsys.readouterr()
    assert len(rows)==44
    assert "✅ Key generated and saved as 'secret.key'" in captured.out
 
def test_encrypt_file(capsys,sample_csv):
    key=Fernet.generate_key()
    encrypt_file(sample_csv,key)
    captured=capsys.readouterr()
    assert f"🔒 File '{sample_csv}' has been encrypted successfully." in captured.out

def test_decrypt_file(capsys,sample_csv):
    key=Fernet.generate_key()
    encrypt_file(sample_csv,key)
    decrypt_file(sample_csv,key)
    captured=capsys.readouterr()
    assert f"🔒 File '{sample_csv}' has been encrypted successfully." in captured.out
    assert f"🔓 File '{sample_csv}' has been decrypted successfully." in captured.out
    


