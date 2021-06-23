%global __brp_check_rpaths %{nil}
%global packname  timedelay
%global packver   1.0.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.11
Release:          3%{?dist}%{?buildtag}
Summary:          Time Delay Estimation for Stochastic Time Series ofGravitationally Lensed Quasars

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.51.3
BuildRequires:    R-CRAN-mvtnorm >= 1.0.11
Requires:         R-MASS >= 7.3.51.3
Requires:         R-CRAN-mvtnorm >= 1.0.11

%description
We provide a toolbox to estimate the time delay between the brightness
time series of gravitationally lensed quasar images via Bayesian and
profile likelihood approaches. The model is based on a state-space
representation for irregularly observed time series data generated from a
latent continuous-time Ornstein-Uhlenbeck process. Our Bayesian method
adopts scientifically motivated hyper-prior distributions and a
Metropolis-Hastings within Gibbs sampler, producing posterior samples of
the model parameters that include the time delay. A profile likelihood of
the time delay is a simple approximation to the marginal posterior
distribution of the time delay. Both Bayesian and profile likelihood
approaches complement each other, producing almost identical results; the
Bayesian way is more principled but the profile likelihood is easier to
implement. A new functionality is added in version 1.0.9 for estimating
the time delay between doubly-lensed light curves observed in two bands.
See also Tak et al. (2017) <doi:10.1214/17-AOAS1027>, Tak et al. (2018)
<doi:10.1080/10618600.2017.1415911>, Hu and Tak (2020) <arXiv:2005.08049>.

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
