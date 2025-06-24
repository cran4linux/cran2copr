%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spatialfusion
%global packver   0.7-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.2
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Analysis of Spatial Data Using a Unifying Spatial Fusion Framework

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rstan 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-CRAN-deldir 
BuildRequires:    R-CRAN-rstantools
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-rstan 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-spam 
Requires:         R-CRAN-deldir 
Requires:         R-CRAN-rstantools

%description
Multivariate modelling of geostatistical (point), lattice (areal) and
point pattern data in a unifying spatial fusion framework. Details are
given in Wang and Furrer (2021) <doi:10.1016/j.csda.2021.107240>. Model
inference is done using either 'Stan' <https://mc-stan.org/> or 'INLA'
<https://www.r-inla.org/>.

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
