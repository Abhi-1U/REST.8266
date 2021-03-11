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
        if path=='':
            from controller.error import path_error
            return path_error()
        else:
            os.mkdir(path)
            return 
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
            from controller.error import path_error
            return path_error()
        else:
            os.rmdir(path)
            return 
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
