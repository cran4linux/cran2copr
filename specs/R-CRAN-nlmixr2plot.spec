%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nlmixr2plot
%global packver   3.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Nonlinear Mixed Effects Models in Population PK/PD, Plot Functions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-nlmixr2est 
BuildRequires:    R-CRAN-nlmixr2extra 
BuildRequires:    R-CRAN-rxode2 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vpc 
BuildRequires:    R-CRAN-xgxr 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-nlmixr2est 
Requires:         R-CRAN-nlmixr2extra 
Requires:         R-CRAN-rxode2 
Requires:         R-utils 
Requires:         R-CRAN-vpc 
Requires:         R-CRAN-xgxr 

%description
Fit and compare nonlinear mixed-effects models in differential equations
with flexible dosing information commonly seen in pharmacokinetics and
pharmacodynamics (Almquist, Leander, and Jirstrand 2015
<doi:10.1007/s10928-015-9409-1>). Differential equation solving is by
compiled C code provided in the 'rxode2' package (Wang, Hallow, and James
2015 <doi:10.1002/psp4.12052>). This package is for 'ggplot2' plotting
methods for 'nlmixr2' objects.

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
