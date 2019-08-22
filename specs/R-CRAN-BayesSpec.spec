%global packname  BayesSpec
%global packver   0.5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.3
Release:          1%{?dist}
Summary:          Bayesian Spectral Analysis Techniques

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-pscl >= 1.4.9
BuildRequires:    R-CRAN-mvtnorm >= 1.0.5
BuildRequires:    R-CRAN-trust >= 0.1.7
Requires:         R-CRAN-pscl >= 1.4.9
Requires:         R-CRAN-mvtnorm >= 1.0.5
Requires:         R-CRAN-trust >= 0.1.7

%description
An implementation of methods for spectral analysis using the Bayesian
framework. It includes functions for modelling spectrum as well as
appropriate plotting and output estimates. There is segmentation
capability with RJ MCMC (Reversible Jump Markov Chain Monte Carlo). The
package takes these methods predominantly from the 2012 paper "AdaptSPEC:
Adaptive Spectral Estimation for Nonstationary Time Series"
<DOI:10.1080/01621459.2012.716340>.

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
%{rlibdir}/%{packname}/INDEX
