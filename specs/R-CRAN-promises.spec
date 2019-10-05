%global packname  promises
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Abstractions for Promise-Based Asynchronous Programming

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-later 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-later 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-magrittr 

%description
Provides fundamental abstractions for doing asynchronous programming in R
using promises. Asynchronous programming is useful for allowing a single R
process to orchestrate multiple tasks in the background while also
attending to something else. Semantics are similar to 'JavaScript'
promises, but with a syntax that is idiomatic R.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
