%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HOIF
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Higher-Order Influence Function Estimators for the Average Treatment Effect

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ustats >= 0.1.5
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-SMUT 
Requires:         R-CRAN-ustats >= 0.1.5
Requires:         R-splines 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-SMUT 

%description
Implements Higher-Order Influence Function (HOIF) estimators of the
Average Treatment Effect (ATE), following Robins et al. (2008)
<doi:10.1214/193940307000000527>, Liu et al. (2017)
<doi:10.48550/arXiv.1705.07577> and Liu and Li (2023)
<doi:10.48550/arXiv.2302.08097>. Estimators of any order are supported,
with optional covariate basis transformations (B-splines, Fourier) and
optional K-fold sample splitting (cross-fitting) for improved
finite-sample performance. The core higher-order U-statistics are computed
exactly via the 'ustats' package, an R interface to the 'Python' package
'u-stats'; the underlying algorithm and its computational complexity are
analyzed in Chen, Zhang and Liu (2025) <doi:10.48550/arXiv.2508.12627>. A
pure R implementation (up to order 6) is also provided as a fallback that
does not require 'Python'.

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
