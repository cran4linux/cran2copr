%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NSO1212
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          National Statistical Office of Mongolia's Open Data API Handler

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.6.0
Requires:         R-core >= 4.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-jsonlite 

%description
The National Statistical Office of Mongolia (NSO) is the national
statistical service and an organization of the Mongolian government. NSO
distributes data sets freely available for open access via its API
<https://www.1212.mn/en/data-base/open-data>. NSO1212 is an R package that
contains functions for effortlessly accessing such data through NSO’s API.
Importing data with the package has an advantage in filtering and tidying
data for further processing and analysis. The functions are compatible
with the API v1.0 and get data sets and detailed information from the API.

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
