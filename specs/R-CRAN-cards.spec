%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cards
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis Results Data

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.1
BuildRequires:    R-CRAN-glue >= 1.6.2
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-tidyselect >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 1.1.2
BuildRequires:    R-CRAN-rlang >= 1.1.1
Requires:         R-CRAN-cli >= 3.6.1
Requires:         R-CRAN-glue >= 1.6.2
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-tidyselect >= 1.2.0
Requires:         R-CRAN-dplyr >= 1.1.2
Requires:         R-CRAN-rlang >= 1.1.1

%description
Construct Clinical Data Interchange Standards Consortium (CDISC) compliant
Analysis Results Data objects. These objects are used and re-used to
construct summary tables, visualizations, and written reports. The package
also exports utilities for working with these objects and creating new
Analysis Results Data objects.

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
