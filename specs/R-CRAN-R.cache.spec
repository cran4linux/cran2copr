%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  R.cache
%global packver   0.17.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.17.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fast and Light-Weight Caching (Memoization) of Objects and Results to Speed Up Computations

License:          LGPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R.utils >= 2.10.1
BuildRequires:    R-CRAN-R.methodsS3 >= 1.8.1
BuildRequires:    R-CRAN-R.oo >= 1.24.0
BuildRequires:    R-CRAN-digest >= 0.6.13
BuildRequires:    R-utils 
Requires:         R-CRAN-R.utils >= 2.10.1
Requires:         R-CRAN-R.methodsS3 >= 1.8.1
Requires:         R-CRAN-R.oo >= 1.24.0
Requires:         R-CRAN-digest >= 0.6.13
Requires:         R-utils 

%description
Memoization can be used to speed up repetitive and computational expensive
function calls.  The first time a function that implements memoization is
called the results are stored in a cache memory.  The next time the
function is called with the same set of parameters, the results are
momentarily retrieved from the cache avoiding repeating the calculations.
With this package, any R object can be cached in a key-value storage where
the key can be an arbitrary set of R objects.  The cache memory is
persistent (on the file system).

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
