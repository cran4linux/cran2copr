%global __brp_check_rpaths %{nil}
%global packname  MMDCopula
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Estimation of Copulas by Maximum Mean Discrepancy

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-VineCopula 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-wdm 
Requires:         R-CRAN-VineCopula 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-wdm 

%description
Provides functions for the robust estimation of parametric families of
copulas using minimization of the Maximum Mean Discrepancy, following the
article Alquier, Chérief-Abdellatif, Derumigny and Fermanian (2022)
<doi:10.1080/01621459.2021.2024836>.

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
