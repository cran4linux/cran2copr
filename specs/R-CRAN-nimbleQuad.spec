%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nimbleQuad
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Laplace Approximation, Quadrature, and Nested Deterministic Approximation Methods for 'nimble'

License:          BSD_3_clause + file LICENSE | GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-nimble >= 1.4.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-polynom 
Requires:         R-CRAN-nimble >= 1.4.0
Requires:         R-methods 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-polynom 

%description
Provides deterministic approximation methods for use with the 'nimble'
package. These include Laplace approximation and higher-order extension of
Laplace approximation using adaptive Gauss-Hermite quadrature (AGHQ), plus
nested deterministic approximation methods related to the 'INLA' approach.
Additional information is available in the NIMBLE User Manual and a
'nimbleQuad' tutorial, both available at
<https://r-nimble.org/documentation.html>.

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
