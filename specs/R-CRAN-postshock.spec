%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  postshock
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Donor-Adjusted Post-Shock Forecasting

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-garchx 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-garchx 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 

%description
Implements donor-adjusted methods for forecasting conditional means and
variances after structural shocks. Historical donor episodes are weighted
using covariates observed before each shock, and their estimated
post-shock effects are combined with forecasts from a target-series model.
The methods build on Lin and Eck (2021)
<doi:10.1016/j.ijforecast.2021.03.010>. The package supports donor
balancing weights, structured donor pools, autoregressive integrated
moving average models, and generalized autoregressive conditional
heteroscedasticity models with external regressors.

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
