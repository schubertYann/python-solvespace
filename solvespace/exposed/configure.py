import sys
import platform
import os.path

py_version = sys.version[0:sys.version.find(" ")]
py_nm = py_version[0:3]
system_machine = platform.machine()

windows_list = {
    "swig":"\"W:\SWIG\swig.exe\"",
    "python":"\""+sys.executable+"\"",
    "python lib":"-LW:/Anaconda3/libs -lPython"+py_nm.replace('.', ''),
    "python include":"-IW:/Anaconda3/include",
    "all":"$(CSO) $(CDEMOEXE) $(PYTHONDLL)",
    "target-directory":"../../pyslvs_library/py"+py_nm.replace('.', '')+"w/ _slvs.pyd libslvs.so slvs.py",
    "Dynamic link library":"$(PYTHONDLL)",
    "library define":"$(DEFLIB) -L. -l:$(CSO)",
    "Executable file":"$(CDEMOEXE)",
    "test":"py"+py_nm.replace('.', '')+"w",
    "pip":"pip",
    }
ubuntu_list = {
    "swig":"swig",
    "python":sys.executable,
    "python lib":"-L/usr/lib/python"+py_nm+"/config-"+py_nm+"m-x86_64-linux-gnu/ -lpython"+py_nm+"m",
    "python include":"-I/usr/include/python"+py_nm+"/",
    "all":"$(CSO) $(CDEMO) $(PYTHONSO)",
    "target-directory":"../../pyslvs_library/py"+py_nm.replace('.', '')+"/ _slvs.so libslvs.so slvs.py",
    "Dynamic link library":"$(PYTHONSO)",
    "library define":"",
    "Executable file":"$(CDEMO)",
    "test":"py"+py_nm.replace('.', ''),
    "pip":"pip3",
    }

def file_check():
    print(str(os.path.isfile('../solvespace.h'))+' | ../solvespace.h')
    print(str(os.path.isfile('../dsc.h'))+' | ../dsc.h')
    print(str(os.path.isfile('../sketch.h'))+' | ../sketch.h')
    print(str(os.path.isfile('../expr.h'))+' | ../expr.h')
    print(str(os.path.isfile('./slvs.h'))+' | ./slvs.h')
    print(str(os.path.isfile('../entity.cpp'))+' | ../entity.cpp')
    print(str(os.path.isfile('../expr.cpp'))+' | ../expr.cpp')
    print(str(os.path.isfile('../constrainteq.cpp'))+' | ../constrainteq.cpp')
    print(str(os.path.isfile('../system.cpp'))+' | ../system.cpp')
    print(str(os.path.isfile('./lib.cpp'))+' | ./lib.cpp')
    print(str(os.path.isfile('./slvs_python.hpp'))+' | ./slvs_python.hpp')
    print(str(os.path.isfile('./slvs.i'))+' | ./slvs.i')
    n = (os.path.isfile('../solvespace.h') and os.path.isfile('../dsc.h') and os.path.isfile('../sketch.h') and
         os.path.isfile('../expr.h') and os.path.isfile('./slvs.h') and os.path.isfile('../entity.cpp') and 
         os.path.isfile('../expr.cpp') and os.path.isfile('../constrainteq.cpp') and os.path.isfile('../system.cpp') and
         os.path.isfile('./lib.cpp') and os.path.isfile('./slvs_python.hpp') and os.path.isfile('./slvs.i')
         )
    return n

def build_Makefile():
    Makefile_script = "#Python Solvespace Makefile"
    if platform.system().lower()=="windows":
        system_list = windows_list
        Makefile_script += """
WIN_DEFINES = -D_WIN32_WINNT=0x500 -D_WIN32_IE=0x500 -DWIN32_LEAN_AND_MEAN
"""
    else: system_list = ubuntu_list
    Makefile_script += """
SWIG = """+system_list["swig"]+"""
PYTHON = """+system_list["python"]+"""
PYTHONLIB = """+system_list["python lib"]+"""
PYTHONINCLUDE = """+system_list["python include"]+"""
DEFINES = -DISOLATION_AWARE_ENABLED -DLIBRARY -DDLL_EXPORT
CFLAGS  = -I../extlib -I../../common/win32 -I. -I.. -D_DEBUG -D_CRT_SECURE_NO_WARNINGS -O2 -g -Wno-write-strings -fpermissive
HEADERS = ../solvespace.h \
../dsc.h \
../sketch.h \
../expr.h \
slvs.h

OBJDIR = ../obj

SSOBJS = $(OBJDIR)/util.obj \
$(OBJDIR)/entity.obj \
$(OBJDIR)/expr.obj \
$(OBJDIR)/constrainteq.obj \
$(OBJDIR)/system.obj

W32OBJS = $(OBJDIR)/w32util.obj
LIBOBJS = $(OBJDIR)/lib.obj

#LIBS = user32.lib gdi32.lib comctl32.lib advapi32.lib shell32.lib
LIBS = 

CFILES = ../win32/w32util.cpp \
../entity.cpp \
../expr.cpp \
../constrainteq.cpp \
../system.cpp \
lib.cpp

OFILES = $(SSOBJS) $(LIBOBJS) $(W32OBJS) $(LIBS)
OWRAP = $(OBJDIR)/slvs_wrap.o
CWRAP = slvs_wrap.cxx
CXX = g++
PYTHONDLL = _slvs.pyd
PYTHONSO = _slvs.so
CSO = libslvs.so
CDEMO = cdemo
CDEMOEXE = CDemo.exe

SONAME = -Wl,-soname,$(PYTHONSO) -o $(PYTHONSO)
DEFLIB = -Wl,--output-def,libslvs.def,--out-implib,libslvs.lib

VPATH = .. ../win32

all: """+system_list["all"]+"""
\t@cp -f --target-directory="""+system_list["target-directory"]+"""
\t@cp -f --target-directory=../../pyslvs_library/"""+system_list["test"]+""" ../../pyslvs_library/__init__.py
\t@echo Complete

test: slvs.py test.py ../../python_test.py
\t@echo ================================
\t@echo Python test
\t@echo --------------------------------
\t@$(PYTHON) ../../python_test.py
\t@echo ================================

install-modules:
\t@echo ================================
\t@echo Python modules for Pyslvs
\t"""+system_list["pip"]+""" install peewee dxfwrite
\t@echo ================================

clean:
\t@rm -f -r ../../pyslvs_library/"""+system_list["test"]+"""/*
\t@rm -f $(OBJDIR)/*.o*
\t@rm -f $(CDEMO)
\t@rm -f $(CDEMOEXE)
\t@rm -f *.so*
\t@rm -f slvs.py
\t@rm -f $(CWRAP)
\t@rm -f *.exe
\t@rm -f *.a
\t@rm -f *.dll
\t@rm -f *.pyd

help:
\t@echo ================================
\t@echo Python Solvespace - Solvespace Library for Python Script
\t@echo Copyright \(C\) 2016 Yuan Chang
\t@echo E-mail: daan0014119@gmail.com
\t@echo --------------------------------
\t@echo Use this Makefile to build Solvespace Library,
\t@echo with Linux or Windows platform and any Python 3
\t@echo version.
\t@echo 
\t@echo Command:
\t@echo all:             Complete compilation process.
\t@echo clean:           Clean all maked files.
\t@echo test:            Test Library with your Python.
\t@echo install-modules  Install Python modules for Pyslvs.
\t@echo help:            Show this help message.
\t@echo ================================

.SECONDEXPANSION:

$(CSO): $(OFILES)
\t@echo --------------------------------
\t@echo Dynamic link library: \"$@\"
\t$(CXX) -shared -o $@ $^
\t@echo --------------------------------

"""+system_list["Dynamic link library"]+""": $(OFILES) $(OWRAP)
\t@echo --------------------------------
\t@echo Dynamic link library: "$@"
\t$(CXX) -shared -o $@ $^ $(PYTHONLIB) """+system_list["library define"]+"""
\t@echo --------------------------------

"""+system_list["Executable file"]+""": CDemo.c $(CSO)
\t@echo ================================
\t@echo Executable file: "$@"
\t@$(CXX) $(CFLAGS) -o $@ $< -L. -l:$(CSO)
\t@echo ================================

$(OBJDIR)/%.obj: %.cpp $(HEADERS)
\t@echo object: "$@"
\t@$(CXX) -fPIC $(CFLAGS) $(DEFINES) -c -o $@ $<

$(CWRAP): slvs.i slvs_python.hpp $(CSO)
\t@echo SWIG: "$@"
\t@$(SWIG) -c++ -python -py3 -o $@ $<

$(OWRAP): $(CWRAP)
\t@echo object: "$@"
\t@$(CXX) -fPIC -I../extlib -I../../common/win32 -I. -I.. -O2 $(DEFINES) -c -o $@ $< $(PYTHONINCLUDE)
"""
    
    with open("./Makefile", 'w', newline="")as f:
        f.write(Makefile_script)
    print("done!")

if __name__=='__main__':
    print("System: "+platform.system())
    print("["+system_machine+"]")
    print("Python Version: "+py_version)
    if file_check():
        print("Files checked done.")
        build_Makefile()
    else: print("Some files not exist.")
