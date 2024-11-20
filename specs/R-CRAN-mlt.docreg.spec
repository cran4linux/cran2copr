%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mlt.docreg
%global packver   1.1-10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.10
Release:          1%{?dist}%{?buildtag}
Summary:          Most Likely Transformations: Documentation and Regression Tests

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-multcomp >= 1.4.4
BuildRequires:    R-CRAN-mlt >= 1.3.2
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-eha 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-flexsurv 
BuildRequires:    R-CRAN-truncreg 
Requires:         R-CRAN-multcomp >= 1.4.4
Requires:         R-CRAN-mlt >= 1.3.2
Requires:         R-CRAN-numDeriv 
Requires:         R-stats 
Requires:         R-CRAN-eha 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-flexsurv 
Requires:         R-CRAN-truncreg 

%description
Additional documentation, a package vignette and regression tests for
package mlt.

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
