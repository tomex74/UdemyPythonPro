cd docs
call sphinx-apidoc -o source/ ../fast_vector/
call make html
cd ..