import gc

def heap_status():
    try:
        data={'free':gc.mem_free(),'allocated':gc.mem_alloc()}
        return data
    except Exception as e:
        print(e)
    finally:
        gc.collect()

def stack_status():
    try:
        import micropython
        used_stack=micropython.stack_use()
        free_stack=8192-used_stack
        data={'used':used_stack,'free':free_stack,'total':8192}
        return data
    except Exception as e:
        print(e)
    finally:
        gc.collect()

def force_gc():
    try:
        from controller.success import success_code
        gc.collect()
        return success_code('OK_GC_1')
    except Exception as e:
        print(e)
    finally:
        gc.collect()
