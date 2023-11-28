%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  renz
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          R-Enzymology

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-VGAM 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-VGAM 

%description
Contains utilities for the analysis of Michaelian kinetic data. Beside the
classical linearization methods (Lineweaver-Burk, Eadie-Hofstee,
Hanes-Woolf and Eisenthal-Cornish-Bowden), features include the ability to
carry out weighted regression analysis that, in most cases, substantially
improves the estimation of kinetic parameters (Aledo (2021)
<doi:10.1002/bmb.21522>). To avoid data transformation and the potential
biases introduced by them, the package also offers functions to directly
fitting data to the Michaelis-Menten equation, either using ([S], v) or
(time, [S]) data. Utilities to simulate substrate progress-curves (making
use of the Lambert W function) are also provided. The package is
accompanied of vignettes that aim to orientate the user in the choice of
the most suitable method to estimate the kinetic parameter of an
Michaelian enzyme.

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
