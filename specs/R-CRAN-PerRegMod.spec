%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PerRegMod
%global packver   4.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fitting Periodic Coefficients Linear Regression Models

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-sn 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-sn 

%description
Provides tools for fitting periodic coefficients regression models to data
where periodicity plays a crucial role. It allows users to model and
analyze relationships between variables that exhibit cyclical or seasonal
patterns, offering functions for estimating parameters and testing the
periodicity of coefficients in linear regression models. For simple
periodic coefficient regression model see Regui et al. (2024)
<doi:10.1080/03610918.2024.2314662>.

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
