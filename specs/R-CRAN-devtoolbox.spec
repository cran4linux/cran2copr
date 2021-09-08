%global __brp_check_rpaths %{nil}
%global packname  devtoolbox
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for the R Developer

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyselect >= 1.0.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-gh 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-flexdashboard 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-ggiraph 
Requires:         R-CRAN-tidyselect >= 1.0.0
Requires:         R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-markdown 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-gh 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-flexdashboard 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-ggiraph 

%description
Reporting tools for the R developer to evaluate their packages in terms of
complexity, usage, and performance. Developers can generate an HTML report
that displays CRAN downloads, number of open GitHub issues and pull
requests, package dependencies, and so on, with each component of the
report available as independent functions.

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
