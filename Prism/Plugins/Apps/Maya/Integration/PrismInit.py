import os, sys, platform


def prismInit(prismArgs=[]):
    Dir = os.path.join(PRISMROOT, "Scripts")

    if Dir not in sys.path:
        sys.path.append(Dir)

    import PrismCore

    pcore = PrismCore.PrismCore(app="Maya", prismArgs=prismArgs)
    return pcore
