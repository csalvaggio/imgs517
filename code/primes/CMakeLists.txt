cmake_minimum_required(VERSION 3.18)
project(primes LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Python COMPONENTS Interpreter Development.Module REQUIRED)

if(NOT Python_EXECUTABLE AND PYTHON_EXECUTABLE)
  set(Python_EXECUTABLE "${PYTHON_EXECUTABLE}")
endif()

execute_process(
  COMMAND "${Python_EXECUTABLE}" -m pybind11 --cmakedir
  OUTPUT_VARIABLE pybind11_dir
  OUTPUT_STRIP_TRAILING_WHITESPACE
)
set(pybind11_DIR "${pybind11_dir}")
find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(_primes src/primes.cpp src/bindings.cpp)

install(TARGETS _primes
  LIBRARY DESTINATION primes
  RUNTIME DESTINATION primes
  ARCHIVE DESTINATION primes
)
