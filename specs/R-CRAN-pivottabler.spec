%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pivottabler
%global packver   1.5.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.4
Release:          1%{?dist}%{?buildtag}
Summary:          Create Pivot Tables

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.2.0
BuildRequires:    R-CRAN-data.table >= 1.10.0
BuildRequires:    R-CRAN-htmlwidgets >= 0.8
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-htmltools >= 0.3.5
Requires:         R-CRAN-R6 >= 2.2.0
Requires:         R-CRAN-data.table >= 1.10.0
Requires:         R-CRAN-htmlwidgets >= 0.8
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-htmltools >= 0.3.5

%description
Create regular pivot tables with just a few lines of R. More complex pivot
tables can also be created, e.g. pivot tables with irregular layouts,
multiple calculations and/or derived calculations based on multiple data
frames.  Pivot tables are constructed using R only and can be written to a
range of output formats (plain text, 'HTML', 'Latex' and 'Excel'),
including with styling/formatting.

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
