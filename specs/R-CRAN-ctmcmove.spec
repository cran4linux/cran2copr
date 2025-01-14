%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ctmcmove
%global packver   1.2.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.10
Release:          1%{?dist}%{?buildtag}
Summary:          Modeling Animal Movement with Continuous-Time Discrete-Space Markov Chains

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-gdistance 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-gdistance 
Requires:         R-CRAN-sp 

%description
Software to facilitates taking movement data in xyt format and pairing it
with raster covariates within a continuous time Markov chain (CTMC)
framework.  As described in Hanks et al. (2015) <DOI:10.1214/14-AOAS803> ,
this allows flexible modeling of movement in response to covariates (or
covariate gradients) with model fitting possible within a Poisson GLM
framework.

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
