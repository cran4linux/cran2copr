%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rio
%global packver   1.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          A Swiss-Army Knife for Data I/O

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.11.2
BuildRequires:    R-CRAN-haven >= 1.1.2
BuildRequires:    R-CRAN-curl >= 0.6
BuildRequires:    R-CRAN-readxl >= 0.1.1
BuildRequires:    R-tools 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-foreign 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-readr 
Requires:         R-CRAN-data.table >= 1.11.2
Requires:         R-CRAN-haven >= 1.1.2
Requires:         R-CRAN-curl >= 0.6
Requires:         R-CRAN-readxl >= 0.1.1
Requires:         R-tools 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-foreign 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-writexl 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-readr 

%description
Streamlined data import and export by making assumptions that the user is
probably willing to make: 'import()' and 'export()' determine the data
format from the file extension, reasonable defaults are used for data
import and export, web-based import is natively supported (including from
SSL/HTTPS), compressed files can be read directly, and fast import
packages are used where appropriate. An additional convenience function,
'convert()', provides a simple method for converting between file types.

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
