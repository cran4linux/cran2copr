%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  strex
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Extra String Manipulation Functions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-checkmate >= 1.9.3
BuildRequires:    R-CRAN-stringi >= 1.7.8
BuildRequires:    R-CRAN-stringr >= 1.5
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-rlang >= 1.0
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-checkmate >= 1.9.3
Requires:         R-CRAN-stringi >= 1.7.8
Requires:         R-CRAN-stringr >= 1.5
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-rlang >= 1.0
Requires:         R-CRAN-lifecycle 
Requires:         R-stats 
Requires:         R-utils 

%description
There are some things that I wish were easier with the 'stringr' or
'stringi' packages. The foremost of these is the extraction of numbers
from strings. 'stringr' and 'stringi' make you figure out the regular
expression for yourself; 'strex' takes care of this for you. There are
many other handy functionalities in 'strex'. Contributions to this package
are encouraged; it is intended as a miscellany of string manipulation
functions that cannot be found in 'stringi' or 'stringr'.

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
