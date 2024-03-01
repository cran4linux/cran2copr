%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SINRELEF.LD
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Reliability and Relative Efficiency in Locally-Dependent Measures

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Implements an approach aimed at assessing the accuracy and effectiveness
of raw scores obtained in scales that contain locally dependent items. The
program uses as input the calibration (structural) item estimates obtained
from fitting extended unidimensional factor-analytic solutions in which
the existing local dependencies are included. Measures of reliability
(Omega) and information are proposed at three levels: (a) total score, (b)
bivariate-doublet, and (c) item-by-item deletion, and are compared to
those that would be obtained if all the items had been locally
independent. All the implemented procedures can be obtained from: (a)
linear factor-analytic solutions in which the item scores are treated as
approximately continuous, and (b) non-linear solutions in which the item
scores are treated as ordered-categorical.

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
