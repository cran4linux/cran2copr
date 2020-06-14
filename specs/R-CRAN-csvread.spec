%global packname  csvread
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          2%{?dist}
Summary:          Fast Specialized CSV File Loader

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15
Requires:         R-core >= 2.15
BuildRequires:    R-methods 
Requires:         R-methods 

%description
Functions for loading large (10M+ lines) CSV and other delimited files,
similar to read.csv, but typically faster and using less memory than the
standard R loader. While not entirely general, it covers many common use
cases when the types of columns in the CSV file are known in advance. In
addition, the package provides a class 'int64', which represents 64-bit
integers exactly when reading from a file. The latter is useful when
working with 64-bit integer identifiers exported from databases. The CSV
file loader supports common column types including 'integer', 'double',
'string', and 'int64', leaving further type transformations to the user.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/10rows_na.csv
%doc %{rlibdir}/%{packname}/10rows.csv
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/csvread_1.0.pdf
%doc %{rlibdir}/%{packname}/csvread_1.1.pdf
%doc %{rlibdir}/%{packname}/csvread_1.2.pdf
%doc %{rlibdir}/%{packname}/genpdfdoc.sh
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
