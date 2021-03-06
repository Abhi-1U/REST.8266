import gc

def heap_status():
    try:
        data={'free':gc.mem_free(),'allocated':gc.mem_alloc()}
        return data
    except Exception as e:
        print(e)
    finally:
        gc.collect()
