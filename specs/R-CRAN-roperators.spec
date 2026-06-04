%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  roperators
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Additional Operators to Help You Write Cleaner R Code

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-tools 
Requires:         R-stats 
Requires:         R-tools 

%description
A set of additional operators and helper functions to make R code easier
to read, write, and maintain. Includes string arithmetic (such as 'foo' +
'bar'), in-place reassignment operators (such as x += 1), logical
operators that handle missing values, floating-point and strict
('JavaScript'-style) equality tests, 'between' operators, and 'SQL'-style
pattern matching. Also provides convenience helpers for type conversion,
operating-system checks, complete-cases statistics, and string
manipulation, such as Oxford-comma pasting and extracting the first, last,
n-th, or most common element of a vector or word in a string. The goal is
to give R users, particularly those coming from other languages such as
'Python', a friendlier and more consistent syntax.

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
