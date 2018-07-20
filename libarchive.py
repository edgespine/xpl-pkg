import zipfile
import os

from  libcommon import dprint,eprint,fn

# Returns True if file extension is zip,rar,7z
def iszip(filename):
    if filename.lower().endswith('zip'):
            dprint( fn() + ": "+ "File" + filename + "is a zip archive")
            return(True)
    else:
        return(False)

def is7z(filename):
    if filename.lower().endswith('7z'):
            dprint( fn() + ": "+ "File" + filename + "is a 7z archive")
            return(True)
    else:
        return(False)

def israr(filename):
    if filename.lower().endswith('rar'):
            dprint( fn() + ": "+ "File" + filename + "is a rar archive")
            return(True)
    else:
        return(False)
# Returns list of matching files (if *.zip)
def isarc(filename):
    import fnmatch
    return (fnmatch.fnmatch(filename,"*.zip"))
# Returns extension if file is an archive
def get_filename_without_extension(path_to_file,ext):
    from os.path import basename,splitext
    base = os.path.basename(path_to_file)
    return(os.path.splitext(base)[0])

def getextension(filename):
    if iszip(filename):
        return(os.path.splitext(filename)[-1].lower())
    else:
        return("")
# Returns extension if file is archive (alternate)
def getextension2(filename):
    if isarc(filename):
        return(os.path.splitext(filename)[-1].lower())
    elif os.path.isdir(filename):
        return("")
    else:
        dprint(fn() + ": " +"File is neither archive or directory")
        return (-2)
    #if os.path.exists()
    #from pathlib import Path
    #p=Path('mmm')
    #p.exists()
# * Get a (validated) list of ZIP files in current directory
def get_zip_file_list(filepath):
    import os, zipfile
    zlist = []
    for filename in os.listdir(filepath):
        if zipfile.is_zipfile(filename):
            zlist.append(filename)
    return (zlist)
# Create a tmp directory and extract zip file into it. Exit if tmp dir already exists
def extract_zip_to_tmp(path_to_zipfile):
    import os
# 1. identify basename and remove .zip extension
    basename = get_filename_without_extension(path_to_zipfile,'.zip')
# 2. identify basedir
    basedir = os.path.dirname(path_to_zipfile)
# 3. new tmp dir name = basedir + "/__tmp__" + basename
    tmp_destination_dir = basedir + "/__tmpdir__" + basename
    #if os.path.exists(tmp_destination_dir): # Don't overwite existsing tmp directory (exit -2)
    #    eprint( fn() + ": "+"tmp directory " + tmp_destination_dir + " alreay exists.")
    #    import sys
    #    sys.exit(-2)
    if os.path.exists(tmp_destination_dir):
        from shutil import rmtree
        rmtree(tmp_destination_dir)
    # Create a tmp directory and extract zipfile into it
    import zipfile
    if zipfile.is_zipfile(path_to_zipfile):
        dprint("* Creating tmp dir: " + tmp_destination_dir)
        os.mkdir(tmp_destination_dir)
        dprint("* Extracting " + path_to_zipfile + " to " + tmp_destination_dir)
        with zipfile.ZipFile(path_to_zipfile, 'r') as z:
            z.extractall(tmp_destination_dir)
    return (tmp_destination_dir)
# Create a tmp directory and extract zip file into it. Exit if tmp dir already exists
def extract_7z_to_tmp(path_to_7zfile):
    import os
    # 1. identify basename and remove .zip extension
    basename = get_filename_without_extension(path_to_7zfile, '.7z')
    # 2. identify basedir
    basedir = os.path.dirname(path_to_7zfile)
    # 3. new tmp dir name = basedir + "/__tmp__" + basename
    tmp_destination_dir = basedir + "/__tmpdir__" + basename

    if os.path.exists(tmp_destination_dir):
        eprint(fn() + ": " +"tmp directory " + tmp_destination_dir + " alreay exists.")
        import sys
        sys.exit(-2)
    else:
        if os.path.exists(path_to_7zfile):
            dprint(fn() + ": " +"* Creating tmp dir: " + tmp_destination_dir)
            os.mkdir(tmp_destination_dir)
            dprint(fn() + ": " +"* Extracting " + path_to_7zfile + " to " + tmp_destination_dir)
            import subprocess
            cmd = '/usr/bin/7z' + ' x "' + path_to_7zfile + '" -o' + tmp_destination_dir
            dprint(fn() + ": " +"Running " + cmd)
            subprocess.call(["7z", "x", path_to_7zfile, '-o' + tmp_destination_dir])
    return(tmp_destination_dir)
# Delete a tmp directory if of the format __tmp_*
def delete_tmp_dir(filepath):
    import os, sys, shutil, re
    if os.path.isdir(filepath):
        if re.search("^__tmpdir__", filepath):
            dprint(fn() + ": " +"* Found " + filepath)
            try:
                dprint(fn() + ": " +"* Removing tmp dir:" + filepath)
                shutil.rmtree(filepath)
                return(0)
            except (OSError, e):
                eprint(fn() + ": " +"ERROR: %s - %s." % (e.filepath, e.strerror))
                return(-1)
        else:
            dprint(fn() + ": " +"* The" + filepath + "is not a tmp directory")
            return(-3)
    else:
        dprint(fn() + ": " +"Directory" + filepath + "not found. Nothing to do.")

def test_zippery():
    for filename in os.listdir('.'):
        ziptmpfilename = ".tmpfile" + filename
        if os.path.exists(ziptmpfilename):
            eprint(fn() + ": " +"ERROR: tmp directory" + ziptmpfilename + " alreay exists.")
            sys.exit(-2)
        else:
            if zipfile.is_zipfile(filename):
                os.mkdir(ziptmpfilename)
                dprint(fn() + ": " +"[" + filename + "] is a Zip file")
                dprint(fn() + ": " +" * Extracting files from" + filename + "...")
                with zipfile.ZipFile(filename, "r") as z:
                    z.extractall(ziptmpfilename)
            else:
                dprint(fn() + ": " +"Is Not Zip ... possibly corrupt")


#dprint( fn() + ": "+ 'y'.join(get_zip_file_list(".")))
#for X in get_zip_file_list("."):
#    delete_tmp_dir("__tmpdir__" + X)
##    extract_zip_to_tmp(X)

#delete_tmp_dir("__tmpdir__" + 'egnxextyremexp11.1.2.7z')
#extract_7z_to_tmp('egnxextyremexp11.1.2.7z')
#