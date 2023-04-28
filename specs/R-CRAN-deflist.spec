%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  deflist
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Deferred List - A Read-Only List-Like Object with Deferred Access

License:          LGPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-assertthat 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-assertthat 

%description
Implements the 'deflist' class, a read-only list-like object that accesses
its elements via a function. The 'deflist' class can be used to model
deferred access to data or computations by routing indexed list access to
a function. This approach is particularly useful when sequential list-like
access to data is required but holding all the data in memory at once is
not feasible. The package also provides utilities for memoisation and
caching to optimize access to frequently requested elements.

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
