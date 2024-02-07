%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  REDCapDM
%global packver   0.9.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.7
Release:          1%{?dist}%{?buildtag}
Summary:          'REDCap' Data Management

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-REDCapR 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-labelled 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-forcats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-REDCapR 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-utils 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-labelled 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-forcats 

%description
REDCap Data Management - REDCapDM is a comprehensive package that enables
users to seamlessly handle data exported directly from REDCap or through
API connections. This tool facilitates various functions, including data
preprocessing, report generation for queries such as outliers or missing
values, and tracking of identified queries. 'REDCap' (Research Electronic
Data CAPture; <https://projectredcap.org>) is a web application developed
at Vanderbilt University, designed for creating and managing online
surveys and databases. The API connection provides users with the
capability to programmatically access both data and project metadata,
including the data dictionary, from the web.

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
