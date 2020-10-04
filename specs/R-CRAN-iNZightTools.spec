%global packname  iNZightTools
%global packver   1.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for 'iNZight'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-readr >= 1.2.0
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-chron 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-validate 
Requires:         R-CRAN-readr >= 1.2.0
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-survey 
Requires:         R-grDevices 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-tools 
Requires:         R-CRAN-chron 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-validate 

%description
Provides a collection of wrapper functions for common variable and dataset
manipulation workflows primarily used by 'iNZight', a graphical user
interface providing easy exploration and visualisation of data for
students of statistics, available in both desktop and online versions.
Additionally, many of the functions return the 'tidyverse' code used to
obtain the result in an effort to bridge the gap between GUI and coding.

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
