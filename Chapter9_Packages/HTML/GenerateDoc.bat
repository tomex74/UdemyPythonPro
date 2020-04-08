cd docs
call sphinx-apidoc -o source/ ../fast_math/
call make html
cd ..