%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tvReg
%global packver   0.5.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.9
Release:          1%{?dist}%{?buildtag}
Summary:          Time-Varying Coefficient for Single and Multi-Equation Regressions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-stats >= 2.14.0
BuildRequires:    R-CRAN-systemfit >= 1.1.20
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-vars 
BuildRequires:    R-CRAN-bvarsv 
BuildRequires:    R-CRAN-plm 
Requires:         R-stats >= 2.14.0
Requires:         R-CRAN-systemfit >= 1.1.20
Requires:         R-CRAN-Matrix 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-vars 
Requires:         R-CRAN-bvarsv 
Requires:         R-CRAN-plm 

%description
Fitting time-varying coefficient models for single and multi-equation
regressions, using kernel smoothing techniques.

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
