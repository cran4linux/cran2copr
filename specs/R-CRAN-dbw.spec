%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dbw
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Doubly Robust Distribution Balancing Weighting Estimation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
Implements the doubly robust distribution balancing weighting proposed by
Katsumata (2024) <doi:10.1017/psrm.2024.23>, which improves the augmented
inverse probability weighting (AIPW) by estimating propensity scores with
estimating equations suitable for the pre-specified parameter of interest
(e.g., the average treatment effects or the average treatment effects on
the treated) and estimating outcome models with the estimated inverse
probability weights. It also implements the covariate balancing propensity
score proposed by Imai and Ratkovic (2014) <doi:10.1111/rssb.12027> and
the entropy balancing weighting proposed by Hainmueller (2012)
<doi:10.1093/pan/mpr025>, both of which use covariate balancing conditions
in propensity score estimation. The point estimate of the parameter of
interest and its uncertainty as well as coefficients for propensity score
estimation and outcome regression are produced using the M-estimation. The
same functions can be used to estimate average outcomes in missing outcome
cases.

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
