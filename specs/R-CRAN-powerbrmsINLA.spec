%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  powerbrmsINLA
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Power Analysis Using 'brms' and 'INLA'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-tibble >= 3.2.0
BuildRequires:    R-CRAN-brms >= 2.19.0
BuildRequires:    R-CRAN-magrittr >= 2.0.0
BuildRequires:    R-CRAN-scales >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-viridisLite >= 0.4.0
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-tibble >= 3.2.0
Requires:         R-CRAN-brms >= 2.19.0
Requires:         R-CRAN-magrittr >= 2.0.0
Requires:         R-CRAN-scales >= 1.2.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-viridisLite >= 0.4.0
Requires:         R-CRAN-pbapply 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides tools for Bayesian power analysis and assurance calculations
using the statistical frameworks of 'brms' and 'INLA'. Includes
simulation-based approaches, support for multiple decision rules
(direction, threshold, ROPE), sequential designs, and visualisation
helpers. Methods are based on Kruschke (2014, ISBN:9780124058880) "Doing
Bayesian Data Analysis: A Tutorial with R, JAGS, and Stan", O'Hagan &
Stevens (2001) <doi:10.1177/0272989X0102100307> "Bayesian Assessment of
Sample Size for Clinical Trials of Cost-Effectiveness", Kruschke (2018)
<doi:10.1177/2515245918771304> "Rejecting or Accepting Parameter Values in
Bayesian Estimation", Rue et al. (2009)
<doi:10.1111/j.1467-9868.2008.00700.x> "Approximate Bayesian inference for
latent Gaussian models by using integrated nested Laplace approximations",
and Bürkner (2017) <doi:10.18637/jss.v080.i01> "brms: An R Package for
Bayesian Multilevel Models using Stan".

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
