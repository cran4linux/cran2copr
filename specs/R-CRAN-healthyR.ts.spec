%global packname  healthyR.ts
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          The Time Series Modeling Companion to 'healthyR'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 0.1.2
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-timetk 
BuildRequires:    R-CRAN-modeltime 
BuildRequires:    R-CRAN-modeltime.ensemble 
BuildRequires:    R-CRAN-modeltime.resample 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyquant 
BuildRequires:    R-CRAN-healthyR.data 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-plotly 
Requires:         R-CRAN-rlang >= 0.1.2
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-timetk 
Requires:         R-CRAN-modeltime 
Requires:         R-CRAN-modeltime.ensemble 
Requires:         R-CRAN-modeltime.resample 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyquant 
Requires:         R-CRAN-healthyR.data 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-plotly 

%description
Hospital time series data analysis workflow tools, modeling, and
automations. This library provides many useful tools to review common
administrative time series hospital data. Some of these include average
length of stay, and readmission rates. The aim is to provide a simple and
consistent verb framework that takes the guesswork out of everything.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
