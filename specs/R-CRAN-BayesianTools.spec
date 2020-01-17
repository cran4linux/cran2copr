%global packname  BayesianTools
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          1%{?dist}
Summary:          General-Purpose MCMC and SMC Samplers and Tools for BayesianStatistics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-emulator 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-CRAN-IDPmisc 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-DHARMa 
BuildRequires:    R-CRAN-gap 
BuildRequires:    R-CRAN-bridgesampling 
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-coda 
Requires:         R-CRAN-emulator 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-tmvtnorm 
Requires:         R-CRAN-IDPmisc 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-msm 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-DHARMa 
Requires:         R-CRAN-gap 
Requires:         R-CRAN-bridgesampling 

%description
General-purpose MCMC and SMC samplers, as well as plot and diagnostic
functions for Bayesian statistics, with a particular focus on calibrating
complex system models. Implemented samplers include various Metropolis
MCMC variants (including adaptive and/or delayed rejection MH), the
T-walk, two differential evolution MCMCs, two DREAM MCMCs, and a
sequential Monte Carlo (SMC) particle filter.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
