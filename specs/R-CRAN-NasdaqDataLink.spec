%global __brp_check_rpaths %{nil}
%global packname  NasdaqDataLink
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          API Wrapper for Nasdaq Data Link

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 0.9.14
BuildRequires:    R-CRAN-httr >= 0.6.1
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-methods 
Requires:         R-CRAN-jsonlite >= 0.9.14
Requires:         R-CRAN-httr >= 0.6.1
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 
Requires:         R-methods 

%description
Functions for interacting directly with the Nasdaq Data Link API to offer
data in a number of formats usable in R, downloading a zip with all data
from a Nasdaq Data Link database, and the ability to search. This R
package uses the Nasdaq Data Link API. For more information go to
<https://docs.data.nasdaq.com/>. For more help on the package itself go to
<https://data.nasdaq.com/tools/r>.

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
