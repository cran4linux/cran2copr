%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fb4package
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          'Fish Bioenergetics 4.0' Model Implementation with High-Performance 'TMB' Backend

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-TMB >= 1.7.0
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-TMB >= 1.7.0
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-Rcpp 

%description
An implementation of the 'Fish Bioenergetics 4.0' framework described in
Deslauriers et al. (2017) <doi:10.1080/03632415.2017.1377558>. Provides
automated parameter optimization, multi-prey diet modeling, and
comprehensive energy budget simulations for fisheries research and
aquaculture applications. An optional 'TMB' (Template Model Builder)
backend delivers 10-50x speedup in maximum likelihood estimation while
maintaining full backward compatibility. Includes species-specific
parameter databases and tools for modeling fish growth, consumption, and
metabolism under varying environmental conditions.

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
