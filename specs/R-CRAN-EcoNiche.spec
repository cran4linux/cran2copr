%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EcoNiche
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Community Niche Position and Width Estimation Tools

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-vegan 

%description
Provides methods for estimating species niche position and niche breadth
under continuous environmental gradients. The package implements canonical
correspondence analysis (CCA), partial CCA (pCCA), generalized additive
models (GAM), and Levins' niche breadth metrics for species-level and
community-level analyses. Methods are based on ter Braak (1986)
<doi:10.2307/1938672>, Okie et al. (2015) <doi:10.1098/rspb.2014.2630>,
Feng et al. (2020) <doi:10.1111/mec.15441>, Wood (2017)
<doi:10.1201/9781315370279>, and Levins (1968, ISBN:978-0691080628).

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
