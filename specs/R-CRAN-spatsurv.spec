%global __brp_check_rpaths %{nil}
%global packname  spatsurv
%global packver   1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Spatial Survival Analysis with Parametric Proportional Hazards Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-spatstat >= 2.0.0
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-spatstat.core 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-spatstat.random 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-RandomFields 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lubridate 
Requires:         R-CRAN-spatstat >= 2.0.0
Requires:         R-CRAN-survival 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-spatstat.core 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-spatstat.random 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-RandomFields 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-methods 
Requires:         R-CRAN-lubridate 

%description
Bayesian inference for parametric proportional hazards spatial survival
models; flexible spatial survival models. See Benjamin M. Taylor, Barry S.
Rowlingson (2017) <doi:10.18637/jss.v077.i04>.

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
