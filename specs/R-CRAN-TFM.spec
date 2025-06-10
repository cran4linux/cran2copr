%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TFM
%global packver   0.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          1%{?dist}%{?buildtag}
Summary:          Sparse Online Principal Component for Truncated Factor Model

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-relliptical 
BuildRequires:    R-CRAN-SOPC 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-relliptical 
Requires:         R-CRAN-SOPC 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-ggplot2 

%description
The Truncated Factor Model is a statistical model designed to handle
specific data structures in data analysis. This R package focuses on the
Sparse Online Principal Component Estimation method, which is used to
calculate data such as the loading matrix and specific variance matrix for
truncated data, thereby better explaining the relationship between common
factors and original variables. Additionally, the R package also provides
other equations for comparison with the Sparse Online Principal Component
Estimation method.The philosophy of the package is described in thesis.
(2023) <doi:10.1007/s00180-022-01270-z>.

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
