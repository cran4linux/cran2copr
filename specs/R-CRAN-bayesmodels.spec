%global packname  bayesmodels
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          The 'Tidymodels' Extension for Bayesian Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 0.1.2
BuildRequires:    R-CRAN-parsnip 
BuildRequires:    R-CRAN-bayesforecast 
BuildRequires:    R-CRAN-bsts 
BuildRequires:    R-CRAN-brms 
BuildRequires:    R-CRAN-BASS 
BuildRequires:    R-CRAN-StanHeaders 
BuildRequires:    R-CRAN-Rlgt 
BuildRequires:    R-CRAN-rstan 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dials 
BuildRequires:    R-CRAN-rsample 
BuildRequires:    R-CRAN-workflows 
BuildRequires:    R-CRAN-modeltime 
BuildRequires:    R-CRAN-timetk 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-rlang >= 0.1.2
Requires:         R-CRAN-parsnip 
Requires:         R-CRAN-bayesforecast 
Requires:         R-CRAN-bsts 
Requires:         R-CRAN-brms 
Requires:         R-CRAN-BASS 
Requires:         R-CRAN-StanHeaders 
Requires:         R-CRAN-Rlgt 
Requires:         R-CRAN-rstan 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dials 
Requires:         R-CRAN-rsample 
Requires:         R-CRAN-workflows 
Requires:         R-CRAN-modeltime 
Requires:         R-CRAN-timetk 
Requires:         R-CRAN-rstantools

%description
Bayesian framework for use with the 'tidymodels' ecosystem. Includes the
following models: Sarima, Garch, Random walk (naive), Additive Linear
State Space Models, Stochastic Volatily Models from 'bayesforecast'
package, Adaptive Splines Surfaces from 'BASS' package and ETS from 'Rlgt'
package.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
