%global packname  yuima
%global packver   1.9.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.6
Release:          3%{?dist}
Summary:          The YUIMA Project Package for SDEs

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildRequires:    R-boot >= 1.3.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-stats4 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-glassoFast 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-boot >= 1.3.2
Requires:         R-CRAN-Rcpp >= 0.12.1
Requires:         R-methods 
Requires:         R-CRAN-zoo 
Requires:         R-stats4 
Requires:         R-utils 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-glassoFast 

%description
Simulation and Inference for SDEs and Other Stochastic Processes.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/AUTHORS
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/ybook
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
