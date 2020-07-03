%global packname  rCAT
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}
Summary:          Conservation Assessment Tools

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-grDevices >= 3.3.2
BuildRequires:    R-CRAN-pracma >= 1.9.5
BuildRequires:    R-CRAN-rgdal >= 1.2.5
BuildRequires:    R-CRAN-sp >= 1.2.3
Requires:         R-grDevices >= 3.3.2
Requires:         R-CRAN-pracma >= 1.9.5
Requires:         R-CRAN-rgdal >= 1.2.5
Requires:         R-CRAN-sp >= 1.2.3

%description
A set of tools and functions to help with species conservation assessments
(Red List threat assessments). Includes Extent of occurrence, Area of
Occupancy, Minimum Enclosing Rectangle, a geographic Projection Wizard and
Species batch processing.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
