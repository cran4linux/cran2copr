%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  allMT
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Acute Lymphoblastic Leukemia Maintenance Therapy Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-tools >= 3.6.1
BuildRequires:    R-utils >= 3.6.1
BuildRequires:    R-CRAN-ggplot2 >= 3.3.6
BuildRequires:    R-CRAN-survival >= 3.2.11
BuildRequires:    R-CRAN-tibble >= 3.1.8
BuildRequires:    R-CRAN-htmlTable >= 2.2.1
BuildRequires:    R-CRAN-plyr >= 1.8.6
BuildRequires:    R-CRAN-reshape2 >= 1.4.4
BuildRequires:    R-CRAN-stringr >= 1.4.1
BuildRequires:    R-CRAN-readxl >= 1.3.1
BuildRequires:    R-CRAN-scales >= 1.2.1
BuildRequires:    R-CRAN-dplyr >= 1.0.10
BuildRequires:    R-CRAN-rio >= 0.5.29
BuildRequires:    R-CRAN-survminer >= 0.4.9
Requires:         R-tools >= 3.6.1
Requires:         R-utils >= 3.6.1
Requires:         R-CRAN-ggplot2 >= 3.3.6
Requires:         R-CRAN-survival >= 3.2.11
Requires:         R-CRAN-tibble >= 3.1.8
Requires:         R-CRAN-htmlTable >= 2.2.1
Requires:         R-CRAN-plyr >= 1.8.6
Requires:         R-CRAN-reshape2 >= 1.4.4
Requires:         R-CRAN-stringr >= 1.4.1
Requires:         R-CRAN-readxl >= 1.3.1
Requires:         R-CRAN-scales >= 1.2.1
Requires:         R-CRAN-dplyr >= 1.0.10
Requires:         R-CRAN-rio >= 0.5.29
Requires:         R-CRAN-survminer >= 0.4.9

%description
Evaluates acute lymphoblastic leukemia maintenance therapy practice at
patient and cohort level.

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
