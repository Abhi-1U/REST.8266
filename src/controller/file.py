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

def read_fs(path):
    try:
        import os
        if path=="":
            iterator=os.ilistdir('/')
            while True:
                try:
                    data=next(iterator)
                except StopIteration:
                    pass
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

    
