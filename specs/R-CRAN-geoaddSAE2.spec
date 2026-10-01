%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geoaddSAE2
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Geoadditive Small Area Estimation for Area-Level Model

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-sae 
BuildRequires:    R-stats 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-sae 
Requires:         R-stats 

%description
Fits area-level geoadditive small area estimation (SAE) models by
extending the Fay-Herriot area-level model with linear, nonlinear, and
spatial effects. The Fay-Herriot model is described by Fay and Herriot
(1979) <doi:10.1080/01621459.1979.10482505>. Geoadditive models combine
nonlinear covariate effects and spatial variation as described by Kammann
and Wand (2003) <doi:10.1111/1467-9876.00385>, while their application to
small area estimation is discussed by Pusponegoro et al. (2019)
<doi:10.21108/JDSA.2019.2.15>. Nonlinear covariate effects are represented
using penalized splines, while spatial effects are represented using a
smooth function of geographic coordinates. Models are estimated using
restricted maximum likelihood (REML), and mean squared error (MSE) is
estimated using a parametric bootstrap. The package also provides
comparisons with the Fay-Herriot and spatial Fay-Herriot (SFH) models.

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
