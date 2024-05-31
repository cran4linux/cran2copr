%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qslice
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Implementations of Various Slice Samplers

License:          MIT + file LICENSE | Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch

%description
Implementations of the quantile slice sampler of Heiner et al. (2024+, in
preparation) as well as other popular slice samplers are provided. Helper
functions for specifying pseudo-target distributions are included, both
for diagnostics and for tuning the quantile slice sampler. Other
implemented methods include the generalized elliptical slice sampler of
Nishihara et al. (2014)<https://jmlr.org/papers/v15/nishihara14a.html},
latent slice sampler of Li and Walker
(2023)<doi:10.1016/j.csda.2022.107652>, and stepping-out slice sampler of
Neal (2003)<doi:10.1214/aos/1056562461>, and independence
Metropolis-Hastings sampler.

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
