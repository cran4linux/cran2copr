%global packname  excerptr
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}
Summary:          Excerpt Structuring Comments from Your Code File and Set a Tableof Contents

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-reticulate 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-reticulate 

%description
This is an R interface to the python package 'excerpts'
(<https://pypi.python.org/pypi/excerpts>).

%prep
%setup -q -c -n %{packname}
find %{packname}/inst -type f -name *.cl -exec chmod a-x {} \;
 find %{packname}/inst -type f -exec sed -Ei 's@#!( )*(/usr)*/bin/(env )*dash@#!/usr/bin/sh@g' {} \;

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/excerpts
%doc %{rlibdir}/%{packname}/runit_tests
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
