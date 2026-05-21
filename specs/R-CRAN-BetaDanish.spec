%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BetaDanish
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          The Beta-Danish Distribution for Lifetime Data Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-tools 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-survival 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-tools 

%description
Implements the four-parameter Beta-Danish distribution and its
three-parameter submodel for survival and reliability analysis, based on
Ahmad and Danish (2025) <doi:10.2478/jamsi-2025-0010>. Provides functions
for density, distribution, quantile, hazard, and random generation.
Includes maximum likelihood estimation for complete and right-censored
data, goodness-of-fit assessment, comparison with standard lifetime
distributions, and publication-quality visualizations. Advanced modules
support Accelerated Failure Time (AFT) regression, mixture and
promotion-time cure models, and competing risks analysis.

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
