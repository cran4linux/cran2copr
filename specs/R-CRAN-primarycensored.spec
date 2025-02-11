%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  primarycensored
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Primary Event Censored Distributions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-rlang 

%description
Provides functions for working with primary event censored distributions
and 'Stan' implementations for use in Bayesian modeling. Primary event
censored distributions are useful for modeling delayed reporting scenarios
in epidemiology and other fields (Charniga et al. (2024)
<doi:10.48550/arXiv.2405.08841>). It also provides support for arbitrary
delay distributions, a range of common primary distributions, and allows
for truncation and secondary event censoring to be accounted for (Park et
al. (2024) <doi:10.1101/2024.01.12.24301247>). A subset of common
distributions also have analytical solutions implemented, allowing for
faster computation. In addition, it provides multiple methods for fitting
primary event censored distributions to data via optional dependencies.

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
