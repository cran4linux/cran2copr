%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  xlsform2word
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Convert 'XLSForm' to Structured 'Word' Document

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-tools 
Requires:         R-CRAN-rlang 

%description
Converts an 'XLSForm' (survey in 'Excel') into a well-structured 'Word'
document, including sections, skip logic, options, and question labels.
Designed to support survey documentation, training materials, and data
collection workflows. The package was developed based on field experience
with 'XLSForm' and humanitarian operations, aiming to streamline
documentation and enhance training efficiency.

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
