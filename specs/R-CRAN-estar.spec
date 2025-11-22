%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  estar
%global packver   1.0-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Ecological Stability Metrics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-zoo 

%description
Standardises and facilitates the use of eleven established stability
properties that have been used to assess systems’ responses to press or
pulse disturbances at different ecological levels (e.g. population,
community). There are two sets of functions. The first set corresponds to
functions that measure stability at any level of organisation, from
individual to community and can be applied to a time series of a system’s
state variables (e.g., body mass, population abundance, or species
diversity). The properties included in this set are: invariability,
resistance, extent and rate of recovery, persistence, and overall
ecological vulnerability. The second set of functions can be applied to
Jacobian matrices. The functions in this set measure the stability of a
community at short and long time scales. In the short term, the
community’s response is measured by maximal amplification, reactivity and
initial resilience (i.e. initial rate of return to equilibrium). In the
long term, stability can be measured as asymptotic resilience and
intrinsic stochastic invariability. Figueiredo et al. (2025)
<doi:10.32942/X2M053>.

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
