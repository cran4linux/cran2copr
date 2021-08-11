%global __brp_check_rpaths %{nil}
%global packname  readr
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Read Rectangular Text Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-vroom >= 1.5.4
BuildRequires:    R-CRAN-hms >= 0.4.1
BuildRequires:    R-CRAN-lifecycle >= 0.2.0
BuildRequires:    R-CRAN-tzdb >= 0.1.1
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-clipr 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-cpp11 
Requires:         R-CRAN-vroom >= 1.5.4
Requires:         R-CRAN-hms >= 0.4.1
Requires:         R-CRAN-lifecycle >= 0.2.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-clipr 
Requires:         R-CRAN-crayon 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-tibble 
Requires:         R-utils 

%description
The goal of 'readr' is to provide a fast and friendly way to read
rectangular data (like 'csv', 'tsv', and 'fwf'). It is designed to
flexibly parse many types of data found in the wild, while still cleanly
failing when data unexpectedly changes.

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
