%global packname  bigtabulate
%global packver   1.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.5
Release:          3%{?dist}
Summary:          Table, Apply, and Split Functionality for Matrix and'big.matrix' Objects

License:          LGPL-3 | Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-bigmemory >= 4.0.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-biganalytics 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-bigmemory >= 4.0.0
Requires:         R-methods 
Requires:         R-CRAN-biganalytics 

%description
Extend the bigmemory package with 'table', 'tapply', and 'split' support
for 'big.matrix' objects. The functions may also be used with native R
matrices for improving speed and memory-efficiency.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
