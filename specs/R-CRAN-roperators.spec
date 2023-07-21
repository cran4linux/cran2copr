%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  roperators
%global packver   1.3.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.14
Release:          1%{?dist}%{?buildtag}
Summary:          Additional Operators to Help you Write Cleaner R Code

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
Provides string arithmetic, reassignment operators, logical operators that
handle missing values, and extra logical operators such as floating point
equality and all or nothing. The intent is to allow R users to write code
that is easier to read, write, and maintain while providing a friendlier
experience to new R users from other language backgrounds (such as
'Python') who are used to concepts such as x += 1 and 'foo' + 'bar'.
Includes operators for not in, easy floating point comparisons, ===
equivalent, and SQL-like like operations (), etc. We also added in some
extra helper functions, such as OS checks, pasting in Oxford comma format,
and functions to get the first, last, nth, or most common element of a
vector or word in a string.

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
