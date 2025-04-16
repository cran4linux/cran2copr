%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  chevron
%global packver   0.2.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.11
Release:          1%{?dist}%{?buildtag}
Summary:          Standard TLGs for Clinical Trials Reporting

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-checkmate >= 2.1.0
BuildRequires:    R-CRAN-tibble >= 2.0.0
BuildRequires:    R-CRAN-lubridate >= 1.7.8
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.4.1
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-forcats >= 1.0.0
BuildRequires:    R-CRAN-glue >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-tern >= 0.9.8
BuildRequires:    R-CRAN-rtables >= 0.6.12
BuildRequires:    R-CRAN-formatters >= 0.5.11
BuildRequires:    R-CRAN-purrr >= 0.3.0
BuildRequires:    R-CRAN-rlistings >= 0.2.11
BuildRequires:    R-CRAN-lifecycle >= 0.2.0
BuildRequires:    R-CRAN-dunlin >= 0.1.10
BuildRequires:    R-CRAN-nestcolor >= 0.1.1
BuildRequires:    R-grid 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-checkmate >= 2.1.0
Requires:         R-CRAN-tibble >= 2.0.0
Requires:         R-CRAN-lubridate >= 1.7.8
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringr >= 1.4.1
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-forcats >= 1.0.0
Requires:         R-CRAN-glue >= 1.0.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-tern >= 0.9.8
Requires:         R-CRAN-rtables >= 0.6.12
Requires:         R-CRAN-formatters >= 0.5.11
Requires:         R-CRAN-purrr >= 0.3.0
Requires:         R-CRAN-rlistings >= 0.2.11
Requires:         R-CRAN-lifecycle >= 0.2.0
Requires:         R-CRAN-dunlin >= 0.1.10
Requires:         R-CRAN-nestcolor >= 0.1.1
Requires:         R-grid 
Requires:         R-methods 
Requires:         R-utils 

%description
Provide standard tables, listings, and graphs (TLGs) libraries used in
clinical trials. This package implements a structure to reformat the data
with 'dunlin', create reporting tables using 'rtables' and 'tern' with
standardized input arguments to enable quick generation of standard
outputs.  In addition, it also provides comprehensive data checks and
script generation functionality.

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
