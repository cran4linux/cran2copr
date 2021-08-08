%global __brp_check_rpaths %{nil}
%global packname  biotools
%global packver   4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Biometry and Applied Statistics in Agricultural Science

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-grDevices 
BuildRequires:    R-datasets 
Requires:         R-CRAN-MASS 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-boot 
Requires:         R-grDevices 
Requires:         R-datasets 

%description
Tools designed to perform and evaluate cluster analysis (including
Tocher's algorithm), discriminant analysis and path analysis (standard and
under collinearity), as well as some useful miscellaneous tools for
dealing with sample size and optimum plot size calculations. A test for
seed sample heterogeneity is now available. Mantel's permutation test can
be found in this package. A new approach for calculating its power is
implemented. biotools also contains tests for genetic covariance
components. Heuristic approaches for performing non-parametric spatial
predictions of generic response variables and spatial gene diversity are
implemented.

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
