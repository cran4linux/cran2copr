%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DENSaftertransform
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimating Density after Logarithmic or Power Transformation of Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Functions for computing: (1) the adaptive normal plug-in(PI) density
estimate for data after the logarithmic transformation; (2) the adaptive
log-normal PI density estimate for data after the power transformation
with an exponent ranging from zero to one; (3) the single-bandwidth PI
density estimate for data after the logarithmic transformation; (4) the
single-bandwidth PI density estimate for data after the power
transformation; (5) the data-driven bandwidth for the single-bandwidth PI
estimator for data after the logarithmic transformation; (6) the
rule-of-thumb bandwidth for the single-bandwidth PI estimator for data
after the power transformation. For details, see the articles: (1)
Savchuk, O. (2026) (submitted). Adaptive log-normal plug-in density
estimator for power transformations. (2) Savchuk, O. (2026). Density
estimation for log-transformed data. Computational Statistics, 41(98)
<doi:10.1007/s00180-026-01766-y>. (3) Savchuk, O., Schick A. (2013).
Density estimation for power transformations. Journal of Nonparametric
Statistics, 25(3), 545-559 <doi:10.1080/10485252.2013.811788>.

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
