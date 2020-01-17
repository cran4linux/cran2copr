%global packname  feasts
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Feature Extraction And Statistics for Time Series

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-tibble >= 1.4.1
BuildRequires:    R-CRAN-tidyr >= 0.8.3
BuildRequires:    R-CRAN-tsibble >= 0.8.0
BuildRequires:    R-CRAN-dplyr >= 0.8.0
BuildRequires:    R-CRAN-rlang >= 0.2.0
BuildRequires:    R-CRAN-fabletools 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-grid 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-tibble >= 1.4.1
Requires:         R-CRAN-tidyr >= 0.8.3
Requires:         R-CRAN-tsibble >= 0.8.0
Requires:         R-CRAN-dplyr >= 0.8.0
Requires:         R-CRAN-rlang >= 0.2.0
Requires:         R-CRAN-fabletools 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-lubridate 
Requires:         R-grid 

%description
Provides a collection of features, decompositions, statistical summaries
and graphics functions for the analysing tidy time series data. The
package name 'feasts' is an acronym comprising of its key features:
Feature Extraction And Statistics for Time Series.

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
