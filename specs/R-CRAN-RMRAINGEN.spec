%global packname  RMRAINGEN
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          RMRAINGEN (R Multi-site RAINfall GENeretor): a package togenerate daily time series of rainfall from monthly mean values

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-RGENERATE 
BuildRequires:    R-CRAN-RMAWGEN 
BuildRequires:    R-CRAN-blockmatrix 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-RGENERATE 
Requires:         R-CRAN-RMAWGEN 
Requires:         R-CRAN-blockmatrix 
Requires:         R-Matrix 

%description
This package contains functions and S3 methods for spatial multi-site
stochastic generation of daily precipitation. It generates precipitation
occurrence in several sites using Wilks' Approach (1998).
Bugs/comments/questions/collaboration of any kind are warmly welcomed.

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
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX
