%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  forecastdom
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for (Un)Conditional Forecast Dominance

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 

%description
A unified toolkit for out-of-sample forecast dominance testing. Covers
unconditional and conditional equal and superior predictive ability,
encompassing, and nested-model comparison. Implements the Diebold-Mariano
test with the Harvey, Leybourne, and Newbold (1997)
<doi:10.1016/S0169-2070(96)00719-4> small-sample correction; the
Clark-West MSFE-adjusted statistic (Clark and West, 2007)
<doi:10.1016/j.jeconom.2006.05.023>; the ENC-NEW encompassing test of
Clark and McCracken (2001) <doi:10.1016/S0304-4076(01)00071-9>; the
Giacomini-White conditional equal predictive ability test (Giacomini and
White, 2006) <doi:10.1111/j.1468-0262.2006.00718.x>; Hansen's superior
predictive ability test (Hansen, 2005) <doi:10.1198/073500105000000063>;
the conditional superior predictive ability test of Li, Liao, and
Quaedvlieg (2022) <doi:10.1093/restud/rdab039>; and the uniform and
average multi-horizon SPA tests of Quaedvlieg (2021)
<doi:10.1080/07350015.2019.1620074>.

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
