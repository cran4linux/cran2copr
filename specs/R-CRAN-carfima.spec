%global __brp_check_rpaths %{nil}
%global packname  carfima
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Continuous-Time Fractionally Integrated ARMA Process forIrregularly Spaced Long-Memory Time Series Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.2.0
Requires:         R-core >= 2.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pracma >= 2.2.9
BuildRequires:    R-CRAN-DEoptim >= 2.2.5
BuildRequires:    R-CRAN-invgamma >= 1.1
BuildRequires:    R-CRAN-truncnorm >= 1.0.8
BuildRequires:    R-CRAN-mvtnorm >= 1.0.11
Requires:         R-CRAN-pracma >= 2.2.9
Requires:         R-CRAN-DEoptim >= 2.2.5
Requires:         R-CRAN-invgamma >= 1.1
Requires:         R-CRAN-truncnorm >= 1.0.8
Requires:         R-CRAN-mvtnorm >= 1.0.11

%description
We provide a toolbox to fit a continuous-time fractionally integrated ARMA
process (CARFIMA) on univariate and irregularly spaced time series data
via both frequentist and Bayesian machinery. A general-order CARFIMA(p, H,
q) model for p>q is specified in Tsai and Chan (2005)
<doi:10.1111/j.1467-9868.2005.00522.x> and it involves p+q+2 unknown model
parameters, i.e., p AR parameters, q MA parameters, Hurst parameter H, and
process uncertainty (standard deviation) sigma. Also, the model can
account for heteroscedastic measurement errors, if the information about
measurement error standard deviations is known. The package produces their
maximum likelihood estimates and asymptotic uncertainties using a global
optimizer called the differential evolution algorithm. It also produces
posterior samples of the model parameters via Metropolis-Hastings within a
Gibbs sampler equipped with adaptive Markov chain Monte Carlo. These
fitting procedures, however, may produce numerical errors if p>2. The
toolbox also contains a function to simulate discrete time series data
from CARFIMA(p, H, q) process given the model parameters and observation
times.

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
%{rlibdir}/%{packname}
