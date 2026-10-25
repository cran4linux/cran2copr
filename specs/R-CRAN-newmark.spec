%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  newmark
%global packver   1.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          Uncertainty Analysis in Dynamic Site and Slope Response

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-mvtnorm 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
Estimates the seismic response of sites and slopes from the results of a
seismic hazard analysis. For a site, it computes the fundamental period of
the soil profile and the amplification of spectral acceleration. For a
slope, it computes the fundamental period, the earthquake-induced
displacement, and the pseudostatic coefficient that keeps a selected
quantile of the displacement within a given limit. Uncertainty in the soil
profile and in the ground motion is represented by Monte Carlo samples.
Every result is reported with its representative value, its applicable
quantiles or dispersion, and the population or conditioning to which it
refers.

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
