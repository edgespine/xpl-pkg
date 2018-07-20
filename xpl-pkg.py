# 1 Unzip/7z and rezip a file

# Simple decrompress to a new tmp dirextory
def scenery_archive_decompress(path_to_archive):
    from libarchive import iszip,is7z,get_filename_without_extension

    from os.path import exists
    if exists(path_to_archive):
        #if str(path_to_archive).lower().endswith('zip'):
        if is7z(path_to_archive):
            from libarchive import extract_7z_to_tmp
            return(extract_7z_to_tmp(path_to_archive))
        elif iszip(path_to_archive):
            from libarchive import extract_zip_to_tmp
            return(extract_zip_to_tmp(path_to_archive))
        else:
            return(-2) # Neither zip nor 7z
# find the custom scenery root witha directory by searching for "Earth nav data"
def scenery_directory_normalise(path_to_directory):
    listofxpdirs = []
    import os
    for root, dirs, files in os.walk(path_to_directory):
        for R in dirs:
            # * At this point 'root' is the correct directory
            if ("Earth nav data" in dirs):
                x = os.path.normpath(root)
                if x not in listofxpdirs:
                    listofxpdirs.append(x)
                return (listofxpdirs)
            listofxpdirs += scenery_directory_normalise(str(root + "/" + R))

    return list_sort_uniq(listofxpdirs)
def demo_find_scenery_root_directory(dir, prefix):
    listofxpdirs=[]
    import os
    for root,dirs,files in os.walk(dir):
        for R in dirs:
#            print(root+"/"+R,"\n")
            if (prefix in dirs) :
                dprint(fn() + ": ", prefix, " prefix found here: ", root + "/" + R, " R == ", R)
#                listofxpdirs.append(root+"/"+str(R))
                return(listofxpdirs)
            listofxpdirs += demo_find_scenery_root_directory(str(R), prefix)
    return(listofxpdirs)
def demo_find_xplane_scenery_directory(dir):
    listofxpdirs=[]
    import os
    for root,dirs,files in os.walk(dir):
# * Scan and detected sub directories
        for R in dirs:
# * At this point 'root' is the correct directory
            if ("Earth nav data" in dirs) :
                dprint(fn() + ": " + "Earth nav data directory found here: " + root)
                listofxpdirs.append(root)
                return(listofxpdirs)
            listofxpdirs += demo_find_xplane_scenery_directory(str(root + "/" + R))
    return(listofxpdirs)
def demofindxpscenery(dir):
    listofxpdirs=[]
    import os
    for root,dirs,files in os.walk(dir):
        for R in dirs:
# * At this point 'root' is the correct directory
            if ("Earth nav data" in dirs) :
#                print(" * Earth nav data directory found here: ",root)
                listofxpdirs.append(root)
                return(listofxpdirs)
            listofxpdirs += demofindxpscenery(str(root + "/" + R))
    return(listofxpdirs)
# * NOTE: Windows paths work in python3 running under cygwin ... who knew!
#listofxpdirs=demo_find_xplane_scenery_directory("/cygdrive/e/X-PLANERY/_CUSTOM_SCENERY/_AIRPORT_TO_BE_SORTED")
#print(listofxpdirs)
#demo_find_xplane_scenery_directory(".")

# Find real scenery root within target directory and move to new directory with new name
def mv_real_root_and_rename(unzipped_airport_directory, icaodb,dst='.'):
    new_file_path = create_name_from_filename(unzipped_airport_directory,icaodb)
    abs_new_filepoath = (mv_to_new_directory(unzipped_airport_directory,new_file_path))
    return abs_new_filepoath

def mv_to_new_directory(real_scenery_root_dir, new_dir):
    from shutil import move
    from os.path import exists
    from libcommon import dprint
    dprint(new_dir)
    if exists(new_dir):
        dprint("Destination already exists.")
        mv_to_new_directory(real_scenery_root_dir, new_dir + ".copy")
    else:
       pass
       move(real_scenery_root_dir, new_dir)  # return code?

    from os.path import abspath
    return (abspath(new_dir))


# * Handling commandline arguments using the argparse module
import argparse,sys,libcommon
#print("First argument = " + sys.argv[1])
parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS, description='Long Options Example')
parser.add_argument('--target', action='store',help="File or Directory to target",default='')
parser.add_argument('--repack', action='store', help='unpack, normalise directory tree and repack',default=False)
parser.add_argument('--type', action='store', help="FREE, EVAL, MINE", default='UNKN')

# * Internal loading of arguments
#print(parser.parse_args([ '--target=','a_AS_Iran_OIIA_Ghazvin-Azadi_v1.01_madmat.7z' ,'--repack',True ]))
# * Show actual command line
# $ python3 xpl_argparsedemo.py --append "HELLO" --prepend "GOODBYE" --noarg=True --files a b c d
# Namespace(files=None, noarg=False, witharg='HI', witharg2='LO')
# Namespace(files=['a', 'b', 'c', 'd'], noarg='True', witharg='HELLO', witharg2='GOODBYE')


print("H")


# The rest of the program can access args thusly:
a=parser.parse_args()
print(a)
# * Example usage and output

#First argument = --prefix
#Namespace(file='venv', files=[], prefix='_a_PREFIXTEST_', suffix='_SUFFIXTEST')
#['_a_PREFIXTEST_venv_SUFFIXTEST']




examplearchives = [ "a_AS_Iran_OIIA_Ghazvin-Azadi_v1.01_madmat.7z" ]


print(" * * TESTING DECOMMPRESION OF ARCHIVES")
unzipped_airport_directory = scenery_archive_decompress(examplearchives)

print(" * * TESTING DIRECTORY TREE NORMALISATION")
print(scenery_directory_normalise(unzipped_airport_directory))

#refactored_file_path = mv_real_root_and_rename(unzipped_airport_directory, icaodb)
#print(refactored_file_path)
