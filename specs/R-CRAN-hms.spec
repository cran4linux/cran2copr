%global packname  hms
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Pretty Time of Day

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-vctrs >= 0.3.8
BuildRequires:    R-CRAN-ellipsis >= 0.3.2
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pkgconfig 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-vctrs >= 0.3.8
Requires:         R-CRAN-ellipsis >= 0.3.2
Requires:         R-CRAN-lifecycle 
Requires:         R-methods 
Requires:         R-CRAN-pkgconfig 
Requires:         R-CRAN-rlang 

%description
Implements an S3 class for storing and formatting time-of-day values,
based on the 'difftime' class.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
