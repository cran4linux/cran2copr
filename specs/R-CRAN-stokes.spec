%global packname  stokes
%global packver   1.0-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          1%{?dist}%{?buildtag}
Summary:          The Exterior Calculus

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-permutations >= 1.0.4
BuildRequires:    R-CRAN-spray >= 1.0.11
BuildRequires:    R-CRAN-partitions 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mathjaxr 
Requires:         R-CRAN-permutations >= 1.0.4
Requires:         R-CRAN-spray >= 1.0.11
Requires:         R-CRAN-partitions 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-mathjaxr 

%description
Provides functionality for working with tensors, alternating tensors,
wedge products, Stokes's theorem, and related concepts from the exterior
calculus.  Functionality for Grassman algebra is provided.  The canonical
reference would be: M. Spivak (1965, ISBN:0-8053-9021-9) "Calculus on
Manifolds".

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
