%global packname  nicheROVER
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Niche Region and Niche Overlap Metrics for Multidimensional Ecological Niches

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.9.0
Requires:         R-core >= 1.9.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Implementation of a probabilistic method to calculate 'nicheROVER'
(_niche_ _r_egion and niche _over_lap) metrics using multidimensional
niche indicator data (e.g., stable isotopes, environmental variables,
etc.). The niche region is defined as the joint probability density
function of the multidimensional niche indicators at a user-defined
probability alpha (e.g., 95%%).  Uncertainty is accounted for in a Bayesian
framework, and the method can be extended to three or more indicator
dimensions.  It provides directional estimates of niche overlap, accounts
for species-specific distributions in multivariate niche space, and
produces unique and consistent bivariate projections of the multivariate
niche region.  The article by Swanson et al. (Ecology, 2015) provides a
detailed description of the methodology.  See the package vignette for a
worked example using fish stable isotope data.

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
