%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  finnts
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Microsoft Finance Time Series Forecasting Framework

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-modeltime 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-Cubist 
BuildRequires:    R-CRAN-dials 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-earth 
BuildRequires:    R-CRAN-feasts 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-hts 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-parsnip 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-recipes 
BuildRequires:    R-CRAN-rsample 
BuildRequires:    R-CRAN-rules 
BuildRequires:    R-CRAN-snakecase 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-timetk 
BuildRequires:    R-CRAN-tune 
BuildRequires:    R-CRAN-vroom 
BuildRequires:    R-CRAN-workflows 
Requires:         R-CRAN-modeltime 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-Cubist 
Requires:         R-CRAN-dials 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-earth 
Requires:         R-CRAN-feasts 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-hts 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-parsnip 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-recipes 
Requires:         R-CRAN-rsample 
Requires:         R-CRAN-rules 
Requires:         R-CRAN-snakecase 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-timetk 
Requires:         R-CRAN-tune 
Requires:         R-CRAN-vroom 
Requires:         R-CRAN-workflows 

%description
Automated time series forecasting developed by Microsoft Finance. The
Microsoft Finance Time Series Forecasting Framework, aka Finn, can be used
to forecast any component of the income statement, balance sheet, or any
other area of interest by finance. Any numerical quantity over time, Finn
can be used to forecast it. While it can be applied outside of the finance
domain, Finn was built to meet the needs of financial analysts to better
forecast their businesses within a company, and has a lot of built in
features that are specific to the needs of financial forecasters. Happy
forecasting!

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
