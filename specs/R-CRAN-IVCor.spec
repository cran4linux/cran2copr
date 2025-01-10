%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  IVCor
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Robust Integrated Variance Correlation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-BwQuant 
BuildRequires:    R-CRAN-quantdr 
BuildRequires:    R-stats 
Requires:         R-splines 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-BwQuant 
Requires:         R-CRAN-quantdr 
Requires:         R-stats 

%description
A integrated variance correlation is proposed to measure the dependence
between a categorical or continuous random variable and a continuous
random variable or vector. This package is designed to estimate the new
correlation coefficient with parametric and nonparametric approaches. Test
of independence for different problems can also be implemented via the new
correlation coefficient with this package.

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
