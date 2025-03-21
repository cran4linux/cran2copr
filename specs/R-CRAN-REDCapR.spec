%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  REDCapR
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interaction Between R and REDCap

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate >= 2.0
BuildRequires:    R-CRAN-readr >= 2.0
BuildRequires:    R-CRAN-tibble >= 2.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-httr >= 1.4.0
BuildRequires:    R-CRAN-dplyr >= 1.0
BuildRequires:    R-CRAN-tidyr >= 1.0
BuildRequires:    R-CRAN-rlang >= 0.4
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-methods 
Requires:         R-CRAN-checkmate >= 2.0
Requires:         R-CRAN-readr >= 2.0
Requires:         R-CRAN-tibble >= 2.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-httr >= 1.4.0
Requires:         R-CRAN-dplyr >= 1.0
Requires:         R-CRAN-tidyr >= 1.0
Requires:         R-CRAN-rlang >= 0.4
Requires:         R-CRAN-jsonlite 
Requires:         R-methods 

%description
Encapsulates functions to streamline calls from R to the REDCap API.
REDCap (Research Electronic Data CAPture) is a web application for
building and managing online surveys and databases developed at Vanderbilt
University.  The Application Programming Interface (API) offers an avenue
to access and modify data programmatically, improving the capacity for
literate and reproducible programming.

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
