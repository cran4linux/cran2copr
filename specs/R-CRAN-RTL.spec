%global packname  RTL
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Risk Tool Library

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-EIAdata 
BuildRequires:    R-CRAN-timetk 
BuildRequires:    R-CRAN-PerformanceAnalytics 
BuildRequires:    R-CRAN-tibbletime 
BuildRequires:    R-CRAN-quantmod 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-tidyquant 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-Quandl 
BuildRequires:    R-CRAN-fGarch 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-tsibble 
BuildRequires:    R-CRAN-feasts 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-fabletools 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-xts 
Requires:         R-stats 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-EIAdata 
Requires:         R-CRAN-timetk 
Requires:         R-CRAN-PerformanceAnalytics 
Requires:         R-CRAN-tibbletime 
Requires:         R-CRAN-quantmod 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-tidyquant 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-Quandl 
Requires:         R-CRAN-fGarch 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-tsibble 
Requires:         R-CRAN-feasts 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-fabletools 

%description
Collection of functions and metadata to complement core packages in
Finance and Commodities, including futures expiry tables and
<http://www.morningstarcommodity.com/> API functions. See
<https://github.com/risktoollib/RTL>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
