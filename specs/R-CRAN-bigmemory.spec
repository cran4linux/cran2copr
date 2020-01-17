%global packname  bigmemory
%global packver   4.5.36
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.5.36
Release:          1%{?dist}
Summary:          Manage Massive Matrices with Shared Memory and Memory-MappedFiles

License:          LGPL-3 | Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-bigmemory.sri 
BuildRequires:    R-CRAN-BH 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-utils 
Requires:         R-CRAN-bigmemory.sri 

%description
Create, store, access, and manipulate massive matrices. Matrices are
allocated to shared memory and may use memory-mapped files.  Packages
'biganalytics', 'bigtabulate', 'synchronicity', and 'bigalgebra' provide
advanced functionality.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
