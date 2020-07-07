%global packname  BayesBEKK
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Bayesian Estimation of Bivariate Volatility Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MTS 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-MTS 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-mvtnorm 

%description
The Multivariate Generalized Autoregressive Conditional Heteroskedasticity
(MGARCH) models are used for modelling the volatile multivariate data
sets. In this package a variant of MGARCH called BEKK (Baba, Engle, Kraft,
Kroner) proposed by Engle and Kroner (1995)
<http://www.jstor.org/stable/3532933> has been used to estimate the
bivariate time series data using Bayesian technique.

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
