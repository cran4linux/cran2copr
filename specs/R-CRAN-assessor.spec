%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  assessor
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Assessment Tools for Regression Models with Discrete and Semicontinuous Outcomes

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-tweedie 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-np 
BuildRequires:    R-CRAN-pscl 
Requires:         R-CRAN-tweedie 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-np 
Requires:         R-CRAN-pscl 

%description
Provides assessment tools for regression models with discrete and
semicontinuous outcomes proposed in Yang (2021)
<doi:10.1080/10618600.2021.1910042>, Yang (2024)
<doi:10.1080/10618600.2024.2303336>, Yang (2024)
<doi:10.1093/biomtc/ujae007>, and Yang (2026) <doi:10.1002/cjs.70046>. It
calculates the double probability integral transform (DPIT) residuals. It
also constructs QQ plots of residuals the ordered curve for assessing mean
structures, quasi-empirical distribution function for overall assessment,
and a formal goodness-of-fit test.

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
