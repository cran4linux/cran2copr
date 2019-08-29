%global packname  mfbvar
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}
Summary:          Mixed-Frequency Bayesian VAR Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.7
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-Rcpp >= 0.12.7
Requires:         R-methods 
Requires:         R-CRAN-pbapply 
Requires:         R-utils 

%description
Estimation of mixed-frequency Bayesian vector autoregressive (VAR) models
with Minnesota or steady-state priors. The package implements a state
space-based VAR model that handles mixed frequencies of the data. The
model is estimated using Markov Chain Monte Carlo to numerically
approximate the posterior distribution, where the prior can be either the
Minnesota prior, as used by Schorfheide and Song (2015)
<doi:10.1080/07350015.2014.954707>, or the steady-state prior, as
advocated by Ankargren, Unosson and Yang (2018)
<http://uu.diva-portal.org/smash/get/diva2:1260262/FULLTEXT01.pdf>.

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
%{rlibdir}/%{packname}/data_prep.R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
