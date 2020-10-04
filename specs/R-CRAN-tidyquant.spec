%global packname  tidyquant
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          2%{?dist}%{?buildtag}
Summary:          Tidy Quantitative Financial Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-timetk >= 2.0.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-quantmod >= 0.4.13
BuildRequires:    R-CRAN-alphavantager >= 0.1.2
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-PerformanceAnalytics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-Quandl 
BuildRequires:    R-CRAN-riingo 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-timeDate 
BuildRequires:    R-CRAN-TTR 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-timetk >= 2.0.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-quantmod >= 0.4.13
Requires:         R-CRAN-alphavantager >= 0.1.2
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-PerformanceAnalytics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-Quandl 
Requires:         R-CRAN-riingo 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-timeDate 
Requires:         R-CRAN-TTR 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-cli 

%description
Bringing business and financial analysis to the 'tidyverse'. The
'tidyquant' package provides a convenient wrapper to various 'xts', 'zoo',
'quantmod', 'TTR' and 'PerformanceAnalytics' package functions and returns
the objects in the tidy 'tibble' format. The main advantage is being able
to use quantitative functions with the 'tidyverse' functions including
'purrr', 'dplyr', 'tidyr', 'ggplot2', 'lubridate', etc. See the
'tidyquant' website for more information, documentation and examples.

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
