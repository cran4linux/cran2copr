%global __brp_check_rpaths %{nil}
%global packname  stableGR
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          A Stable Gelman-Rubin Diagnostic for Markov Chain Monte Carlo

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-mcmcse >= 1.4.1
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-mcmcse >= 1.4.1
Requires:         R-CRAN-mvtnorm 

%description
Practitioners of Bayesian statistics often use Markov chain Monte Carlo
(MCMC) samplers to sample from a posterior distribution. This package
determines whether the MCMC sample is large enough to yield reliable
estimates of the target distribution. In particular, this calculates a
Gelman-Rubin convergence diagnostic using stable and consistent estimators
of Monte Carlo variance. Additionally, this uses the connection between an
MCMC sample's effective sample size and the Gelman-Rubin diagnostic to
produce a threshold for terminating MCMC simulation. Finally, this informs
the user whether enough samples have been collected and (if necessary)
estimates the number of samples needed for a desired level of accuracy.
The theory underlying these methods can be found in "Revisiting the
Gelman-Rubin Diagnostic" by Vats and Knudson (2018) <arXiv:1812:09384>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/INDEX
