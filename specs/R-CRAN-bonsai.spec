%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bonsai
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Model Wrappers for Tree-Based Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-parsnip >= 1.0.1
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dials 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-parsnip >= 1.0.1
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dials 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-utils 
Requires:         R-CRAN-withr 

%description
Bindings for additional tree-based model engines for use with the
'parsnip' package. Models include gradient boosted decision trees with
'LightGBM' (Ke et al, 2017.), conditional inference trees and conditional
random forests with 'partykit' (Hothorn and Zeileis, 2015. and Hothorn et
al, 2006. <doi:10.1198/106186006X133933>), and accelerated oblique random
forests with 'aorsf' (Jaeger et al, 2022 <doi:10.5281/zenodo.7116854>).

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
