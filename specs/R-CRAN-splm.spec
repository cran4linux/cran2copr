%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  splm
%global packver   1.6-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.5
Release:          1%{?dist}%{?buildtag}
Summary:          Econometric Models for Spatial Panel Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.12.0
Requires:         R-core >= 2.12.0
BuildArch:        noarch
BuildRequires:    R-CRAN-spatialreg >= 1.2.1
BuildRequires:    R-CRAN-spdep >= 1.2.1
BuildRequires:    R-CRAN-plm 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-bdsmatrix 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-spatialreg >= 1.2.1
Requires:         R-CRAN-spdep >= 1.2.1
Requires:         R-CRAN-plm 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-bdsmatrix 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-spam 
Requires:         R-methods 
Requires:         R-CRAN-stringr 

%description
ML and GM estimation and diagnostic testing of econometric models for
spatial panel data.

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
