%global packname  covr
%global packver   3.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3.1
Release:          1%{?dist}
Summary:          Test Coverage for Packages

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-withr >= 1.0.2
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-rex 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-withr >= 1.0.2
Requires:         R-methods 
Requires:         R-CRAN-digest 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-rex 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-yaml 

%description
Track and report code coverage for your package and (optionally) upload
the results to a coverage service like 'Codecov' <http://codecov.io> or
'Coveralls' <http://coveralls.io>. Code coverage is a measure of the
amount of code being exercised by a set of tests. It is an indirect
measure of test quality and completeness. This package is compatible with
any testing methodology or framework and tracks coverage of both R code
and compiled C/C++/FORTRAN code.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/rstudio
%doc %{rlibdir}/%{packname}/www
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
