%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  easy.utils
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Frequently Used Functions for Easy R Programming

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fastmatch 
BuildRequires:    R-CRAN-Polychrome 
BuildRequires:    R-CRAN-randomcoloR 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
Requires:         R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fastmatch 
Requires:         R-CRAN-Polychrome 
Requires:         R-CRAN-randomcoloR 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 

%description
Some utility functions for validation, data manipulation or color
palettes. These functions can be helpful to reduce internal codes
everywhere in package development.

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
