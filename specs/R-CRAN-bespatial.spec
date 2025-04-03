%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bespatial
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Boltzmann Entropy for Spatial Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-terra >= 1.5.13
BuildRequires:    R-CRAN-comat >= 0.9.2
BuildRequires:    R-CRAN-belg 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-landscapemetrics 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-terra >= 1.5.13
Requires:         R-CRAN-belg 
Requires:         R-CRAN-comat >= 0.9.2
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-landscapemetrics 

%description
Calculates several entropy metrics for spatial data inspired by
Boltzmann's entropy formula. It includes metrics introduced by Cushman for
landscape mosaics (Cushman (2015) <doi:10.1007/s10980-015-0305-2>), and
landscape gradients and point patterns (Cushman (2021)
<doi:10.3390/e23121616>); by Zhao and Zhang for landscape mosaics (Zhao
and Zhang (2019) <doi:10.1007/s10980-019-00876-x>); and by Gao et al. for
landscape gradients (Gao et al. (2018) <doi:10.1111/tgis.12315>; Gao and
Li (2019) <doi:10.1007/s10980-019-00854-3>).

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
