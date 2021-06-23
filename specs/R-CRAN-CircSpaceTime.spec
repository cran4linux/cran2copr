%global __brp_check_rpaths %{nil}
%global packname  CircSpaceTime
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          3%{?dist}%{?buildtag}
Summary:          Spatial and Spatio-Temporal Bayesian Model for Circular Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.12.14
BuildRequires:    R-CRAN-circular 
BuildRequires:    R-CRAN-RInside 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.14
Requires:         R-CRAN-circular 
Requires:         R-CRAN-RInside 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-ggplot2 

%description
Implementation of Bayesian models for spatial and spatio-temporal
interpolation of circular data using Gaussian Wrapped and Gaussian
Projected distributions. We developed the methods described in Jona
Lasinio G. et al. (2012) <doi: 10.1214/12-aoas576>, Wang F. et al. (2014)
<doi: 10.1080/01621459.2014.934454> and Mastrantonio G. et al. (2016)
<doi: 10.1007/s11749-015-0458-y>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
