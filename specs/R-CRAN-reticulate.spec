%global packname  reticulate
%global packver   1.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.13
Release:          1%{?dist}
Summary:          Interface to 'Python'

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    python >= 2.7.0
BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.7
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-Rcpp >= 0.12.7
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-jsonlite 
Requires:         R-Matrix 

%description
Interface to 'Python' modules, classes, and functions. When calling into
'Python', R data types are automatically converted to their equivalent
'Python' types. When values are returned from 'Python' to R they are
converted back to R types. Compatible with all versions of 'Python' >=
2.7.

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
%doc %{rlibdir}/%{packname}/config
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/python
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
