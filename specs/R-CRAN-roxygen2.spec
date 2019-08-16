%global packname  roxygen2
%global packver   6.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.1.1
Release:          1%{?dist}
Summary:          In-Line Documentation for R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-R6 >= 2.1.2
BuildRequires:    R-CRAN-desc >= 1.2.0
BuildRequires:    R-CRAN-pkgload >= 1.0.2
BuildRequires:    R-CRAN-stringr >= 1.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-brew 
BuildRequires:    R-CRAN-commonmark 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-R6 >= 2.1.2
Requires:         R-CRAN-desc >= 1.2.0
Requires:         R-CRAN-pkgload >= 1.0.2
Requires:         R-CRAN-stringr >= 1.0.0
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-brew 
Requires:         R-CRAN-commonmark 
Requires:         R-CRAN-digest 
Requires:         R-methods 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringi 
Requires:         R-utils 
Requires:         R-CRAN-xml2 

%description
Generate your Rd documentation, 'NAMESPACE' file, and collation field
using specially formatted comments. Writing documentation in-line with
code makes it easier to keep your documentation up-to-date as your
requirements change. 'Roxygen2' is inspired by the 'Doxygen' system for
C++.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
