%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  admiralmetabolic
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Metabolism Extension Package for ADaM in 'R' Asset Library

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.2
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-admiraldev >= 1.2.0
BuildRequires:    R-CRAN-admiral >= 1.1.1
BuildRequires:    R-CRAN-tidyselect >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.4
BuildRequires:    R-CRAN-rlang >= 0.4.4
BuildRequires:    R-CRAN-purrr >= 0.3.3
BuildRequires:    R-CRAN-lifecycle >= 0.1.0
Requires:         R-CRAN-cli >= 3.6.2
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-admiraldev >= 1.2.0
Requires:         R-CRAN-admiral >= 1.1.1
Requires:         R-CRAN-tidyselect >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.4
Requires:         R-CRAN-rlang >= 0.4.4
Requires:         R-CRAN-purrr >= 0.3.3
Requires:         R-CRAN-lifecycle >= 0.1.0

%description
A toolbox for programming Clinical Data Standards Interchange Consortium
(CDISC) compliant Analysis Data Model (ADaM) datasets in R. ADaM datasets
are a mandatory part of any New Drug or Biologics License Application
submitted to the United States Food and Drug Administration (FDA).
Analysis derivations are implemented in accordance with the "Analysis Data
Model Implementation Guide" (CDISC Analysis Data Model Team, 2021,
<https://www.cdisc.org/standards/foundational/adam>).  The package is an
extension package of the 'admiral' package focusing on the metabolism
therapeutic area.

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
