%global packname  BTR
%global packver   1.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.4
Release:          1%{?dist}
Summary:          Training and Analysing Asynchronous Boolean Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.3
Requires:         R-core >= 3.0.3
BuildRequires:    R-CRAN-foreach >= 1.4.1
BuildRequires:    R-CRAN-entropy >= 1.2.1
BuildRequires:    R-CRAN-infotheo >= 1.2.0
BuildRequires:    R-CRAN-doParallel >= 1.0.8
BuildRequires:    R-CRAN-igraph >= 1.0.1
BuildRequires:    R-CRAN-diptest >= 0.75.7
BuildRequires:    R-CRAN-poweRlaw >= 0.30.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.4
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
Requires:         R-CRAN-foreach >= 1.4.1
Requires:         R-CRAN-entropy >= 1.2.1
Requires:         R-CRAN-infotheo >= 1.2.0
Requires:         R-CRAN-doParallel >= 1.0.8
Requires:         R-CRAN-igraph >= 1.0.1
Requires:         R-CRAN-diptest >= 0.75.7
Requires:         R-CRAN-poweRlaw >= 0.30.0
Requires:         R-CRAN-Rcpp >= 0.11.4
Requires:         R-methods 
Requires:         R-parallel 

%description
Tools for inferring asynchronous Boolean models from single-cell
expression data.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
