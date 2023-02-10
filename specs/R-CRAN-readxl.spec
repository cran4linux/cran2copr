%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  readxl
%global packver   1.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Read Excel Files

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-tibble >= 2.0.1
BuildRequires:    R-CRAN-cpp11 >= 0.4.0
BuildRequires:    R-CRAN-cellranger 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-progress 
Requires:         R-CRAN-tibble >= 2.0.1
Requires:         R-CRAN-cellranger 
Requires:         R-utils 

%description
Import excel files into R. Supports '.xls' via the embedded 'libxls' C
library <https://github.com/libxls/libxls> and '.xlsx' via the embedded
'RapidXML' C++ library <https://rapidxml.sourceforge.net/>. Works on
Windows, Mac and Linux without external dependencies.

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
