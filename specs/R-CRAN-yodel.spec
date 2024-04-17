%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  yodel
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          A General Bayesian Model Averaging Helper

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.0
BuildRequires:    R-CRAN-rlang >= 0.4
BuildRequires:    R-CRAN-purrr >= 0.3
Requires:         R-CRAN-dplyr >= 1.0
Requires:         R-CRAN-rlang >= 0.4
Requires:         R-CRAN-purrr >= 0.3

%description
Provides helper functions to perform Bayesian model averaging using Markov
chain Monte Carlo samples from separate models. Calculates weights and
obtains draws from the model-averaged posterior for quantities of interest
specified by the user. Weight calculations can be done using marginal
likelihoods or log-predictive likelihoods as in Ando, T., & Tsay, R.
(2010) <doi:10.1016/j.ijforecast.2009.08.001>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
