%global packname  mixR
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}
Summary:          Finite Mixture Modeling for Raw and Binned Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ggplot2 >= 2.1.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.8
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 2.1.0
Requires:         R-CRAN-Rcpp >= 0.12.8
Requires:         R-graphics 
Requires:         R-stats 

%description
Performs maximum likelihood estimation for finite mixture models for
families including Normal, Weibull, Gamma and Lognormal by using EM
algorithm, together with Newton-Raphson algorithm or bisection method when
necessary. It also conducts mixture model selection by using information
criteria or bootstrap likelihood ratio test. The data used for mixture
model fitting can be raw data or binned data. The model fitting process is
accelerated by using R package 'Rcpp'.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
