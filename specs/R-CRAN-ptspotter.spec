%global __brp_check_rpaths %{nil}
%global packname  ptspotter
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Helper Functions for Use with "ProjectTemplate"

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-beepr >= 1.3
BuildRequires:    R-CRAN-log4r >= 0.3.2
BuildRequires:    R-CRAN-this.path >= 0.2.0
BuildRequires:    R-CRAN-pryr >= 0.1.4
BuildRequires:    R-utils 
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-beepr >= 1.3
Requires:         R-CRAN-log4r >= 0.3.2
Requires:         R-CRAN-this.path >= 0.2.0
Requires:         R-CRAN-pryr >= 0.1.4
Requires:         R-utils 

%description
Utility functions produced specifically for (but not limited to) working
with 'ProjectTemplate' data pipelines. This package helps to quickly
create and manage sequentially numbered scripts, quickly set up logging
with 'log4r' and functions to help debug and monitor procedures.

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
