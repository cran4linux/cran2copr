%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GeneralizedHyperbolic
%global packver   0.8-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.6
Release:          1%{?dist}%{?buildtag}
Summary:          The Generalized Hyperbolic Distribution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-DistributionUtils 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-DistributionUtils 
Requires:         R-CRAN-MASS 

%description
Functions for the hyperbolic and related distributions. Density,
distribution and quantile functions and random number generation are
provided for the hyperbolic distribution, the generalized hyperbolic
distribution, the generalized inverse Gaussian distribution and the
skew-Laplace distribution. Additional functionality is provided for the
hyperbolic distribution, normal inverse Gaussian distribution and
generalized inverse Gaussian distribution, including fitting of these
distributions to data. Linear models with hyperbolic errors may be fitted
using hyperblmFit.

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
