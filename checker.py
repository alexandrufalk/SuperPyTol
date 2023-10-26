
import keyboard
while 1:
    if keyboard.is_pressed("Ctrl+r"):
        with open('test.py','r') as file:
            file_data=file.read()
            file_data_start_index=file_data.find("'@Start@'")
            file_data_end_index=file_data.find("'@End@'")
            exec_command=file_data[file_data_start_index:file_data_end_index]
            with open('exec_log.txt','w') as txt_file:
                txt_file.write(exec_command)