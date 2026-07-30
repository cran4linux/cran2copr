%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  koma
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Simultaneous Equation Models for Forecasting

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-utils >= 4.4.1
BuildRequires:    R-stats >= 4.0.2
BuildRequires:    R-CRAN-cli >= 3.6.3
BuildRequires:    R-CRAN-glue >= 1.8.0
BuildRequires:    R-CRAN-Matrix >= 1.5.4.1
BuildRequires:    R-CRAN-foreach >= 1.5.2
BuildRequires:    R-CRAN-rlang >= 1.1.6
BuildRequires:    R-CRAN-tempdisagg >= 1.1
BuildRequires:    R-CRAN-purrr >= 1.0.4
BuildRequires:    R-CRAN-doFuture >= 1.0.0
BuildRequires:    R-CRAN-progressr >= 0.15.0
BuildRequires:    R-methods 
Requires:         R-utils >= 4.4.1
Requires:         R-stats >= 4.0.2
Requires:         R-CRAN-cli >= 3.6.3
Requires:         R-CRAN-glue >= 1.8.0
Requires:         R-CRAN-Matrix >= 1.5.4.1
Requires:         R-CRAN-foreach >= 1.5.2
Requires:         R-CRAN-rlang >= 1.1.6
Requires:         R-CRAN-tempdisagg >= 1.1
Requires:         R-CRAN-purrr >= 1.0.4
Requires:         R-CRAN-doFuture >= 1.0.0
Requires:         R-CRAN-progressr >= 0.15.0
Requires:         R-methods 

%description
Estimate and forecast Bayesian simultaneous equation models for
macroeconomic time series. Provides tools to specify systems of behavioral
equations and accounting identities, transform and manage time series,
simulate from the posterior using a Metropolis-within-Gibbs sampler, and
generate unconditional and conditional forecasts with user-defined priors
and restrictions. Methods are described in Rathke A. and Sarferaz S.
(forthcoming) "Bayesian Estimation of Simultaneous Equations Model".

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
