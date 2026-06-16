%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  baytaAAR
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Transition Analysis with Markov Chain Monte Carlo

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-nimble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-scoringRules 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-flexsurv 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-stats 
Requires:         R-CRAN-nimble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-scoringRules 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-flexsurv 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-checkmate 
Requires:         R-stats 

%description
Provides Bayesian age estimation for bioarchaeological skeletal data using
ordinal probit regression models implemented in 'JAGS' and 'NIMBLE'. The
package is designed to handle multiple ordinal traits of adult individuals
and incorporates a Gompertz prior on age to reflect population-level
mortality. It accounts for estimation uncertainties and supports full
customization of model parameters and Markov Chain Monte Carlo settings.
For more details see Müller-Scheeßel et al. (2026)
<doi:10.1002/ajpa.70289>.

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
