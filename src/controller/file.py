import gc

def ls_file(path):
    try:
        import os
        if path=="":
            data=os.listdir()
            directory={'/':data}
            return directory
        else :
            data=os.listdir(path)
            directory={path:data}
            return directory
    except OSError as OSE:
        return {path:None}
    except Exception as e:
        print(e)
    finally:
        gc.collect()

def make_folder(path):
    try:
        import os
        if path=='' or path==None:
            from controller.error import raise_error
            return raise_error('ERR_FS_1')
        else:
            from controller.success import success_code
            os.mkdir(path)
            return success_code('OK_FS_1')
    except OSError as OSE:
        return {path:None}
    except Exception as e:
        print(e)
    finally:
        gc.collect()
        
def remove_folder(path):
    try:
        import os
        if path=='':
            from controller.error import raise_error
            return raise_error('ERR_FS_1')
        else:
            gc.collect()
            from controller.success import success_code
            from controller.access import check_path
            if check_path(path):
                os.rmdir(path)
            return success_code('OK_FS_2')
    except OSError as OSE:
        return {path:None}
    except Exception as e:
        print(e)
    finally:
        gc.collect()

def get_cwd():
    try:
        import os
        data={'cwd':os.getcwd()}
        return data
    except OSError as OSE:
        return {path:None}
    except Exception as e:
        print(e)
    finally:
        gc.collect()
        
def change_dir(path):
    try:
        import os
        if path=='':
            from controller.error import path_error
            return path_error()
        else:
            os.chdir(path)
 
    except OSError as OSE:
        return {path:None}
    except Exception as e:
        print(e)
    finally:
        gc.collect()

def remove_file(path):
    try:
        import os
        from controller.success import success_code
        if path=='':
            from controller.error import raise_error
            return raise_error('ERR_FS_1')
        else:
            os.remove(path)
            return success_code('OK_FS_5')
    except OSError as OSE:
        return {path:None}
    except Exception as e:
        print(e)
    finally:
        gc.collect()

def rename(path,newname):
    try:
        import os
        from controller.success import success_code
        if path=='':
            from controller.error import raise_error
            return raise_error('ERR_FS_1')
        else:
            os.rename(path,newname)
            return success_code('OK_FS_4')
    except OSError as OSE:
        return {path:None}
    except Exception as e:
        print(e)
    finally:
        gc.collect()
