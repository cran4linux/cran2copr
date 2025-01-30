%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PopulateR
%global packver   1.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.13
Release:          1%{?dist}%{?buildtag}
Summary:          Create Data Frames for the Micro-Simulation of Human Populations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-brainGraph >= 3.1.0
BuildRequires:    R-CRAN-withr >= 3.0.2
BuildRequires:    R-CRAN-igraph >= 2.1.1
BuildRequires:    R-CRAN-sn >= 2.1.1
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-plyr >= 1.8.9
BuildRequires:    R-CRAN-PearsonDS >= 1.3.1
BuildRequires:    R-CRAN-tidyr >= 1.3.1
BuildRequires:    R-CRAN-tidyselect >= 1.2.1
BuildRequires:    R-CRAN-data.table >= 1.16.2
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-rlang >= 1.1.4
Requires:         R-CRAN-brainGraph >= 3.1.0
Requires:         R-CRAN-withr >= 3.0.2
Requires:         R-CRAN-igraph >= 2.1.1
Requires:         R-CRAN-sn >= 2.1.1
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-plyr >= 1.8.9
Requires:         R-CRAN-PearsonDS >= 1.3.1
Requires:         R-CRAN-tidyr >= 1.3.1
Requires:         R-CRAN-tidyselect >= 1.2.1
Requires:         R-CRAN-data.table >= 1.16.2
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-rlang >= 1.1.4

%description
Tools for constructing detailed synthetic human populations from frequency
tables. Add ages based on age groups and sex, create households, add
students to education facilities, create employers, add employers to
employees, and create interpersonal networks.

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
