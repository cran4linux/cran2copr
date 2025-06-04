%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  adsoRptionCV
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Cross-Validation Methods for Adsorption Isotherm Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-nls2 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-nls2 
Requires:         R-graphics 

%description
Provides cross-validation tools for adsorption isotherm models, supporting
both linear and non-linear forms. Current methods cover commonly used
isotherms including the Freundlich, Langmuir, and Temkin models. This
package implements K-fold and leave-one-out cross-validation (LOOCV) with
optional clustering-based fold assignment to preserve underlying data
structures during validation. Model predictive performance is assessed
using mean squared error (MSE), with optional graphical visualization of
fold-wise MSEs to support intuitive evaluation of model accuracy. This
package is intended to facilitate rigorous model validation in adsorption
studies and aid researchers in selecting robust isotherm models. For more
details, see Montgomery et al. (2012) <isbn: 978-0-470-54281-1>, Lumumba
et al. (2024) <doi:10.11648/j.ajtas.20241305.13>, and Yates et al. (2022)
<doi:10.1002/ecm.1557>.

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
