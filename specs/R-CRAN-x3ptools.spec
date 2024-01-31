%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  x3ptools
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Working with 3D Surface Measurements

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3
BuildRequires:    R-CRAN-pracma >= 2.4.0
BuildRequires:    R-CRAN-yaml >= 2.3.7
BuildRequires:    R-CRAN-readr >= 2.1.0
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-zoo >= 1.8
BuildRequires:    R-CRAN-xml2 >= 1.3.5
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-scales >= 1.2.1
BuildRequires:    R-CRAN-rgl >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-purrr >= 1.0.0
BuildRequires:    R-CRAN-digest >= 0.6
BuildRequires:    R-CRAN-imager >= 0.45.2
BuildRequires:    R-CRAN-assertthat >= 0.2.1
BuildRequires:    R-CRAN-png >= 0.1.7
BuildRequires:    R-grDevices 
Requires:         R-CRAN-MASS >= 7.3
Requires:         R-CRAN-pracma >= 2.4.0
Requires:         R-CRAN-yaml >= 2.3.7
Requires:         R-CRAN-readr >= 2.1.0
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-zoo >= 1.8
Requires:         R-CRAN-xml2 >= 1.3.5
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-scales >= 1.2.1
Requires:         R-CRAN-rgl >= 1.2.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-purrr >= 1.0.0
Requires:         R-CRAN-digest >= 0.6
Requires:         R-CRAN-imager >= 0.45.2
Requires:         R-CRAN-assertthat >= 0.2.1
Requires:         R-CRAN-png >= 0.1.7
Requires:         R-grDevices 

%description
The x3p file format is specified in ISO standard 5436:2000 to describe 3d
surface measurements. 'x3ptools' allows reading, writing and basic
modifications to the 3D surface measurements.

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
