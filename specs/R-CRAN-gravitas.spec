%global packname  gravitas
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Explore Probability Distributions for Bivariate TemporalGranularities

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.3
Requires:         R-core >= 3.1.3
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.1.1
BuildRequires:    R-CRAN-tibble >= 2.1.1
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-tidyr >= 0.8.3
BuildRequires:    R-CRAN-dplyr >= 0.8.0
BuildRequires:    R-CRAN-tsibble >= 0.8.0
BuildRequires:    R-CRAN-rlang >= 0.3.4
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lvplot 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-ineq 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.1.1
Requires:         R-CRAN-tibble >= 2.1.1
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-tidyr >= 0.8.3
Requires:         R-CRAN-dplyr >= 0.8.0
Requires:         R-CRAN-tsibble >= 0.8.0
Requires:         R-CRAN-rlang >= 0.3.4
Requires:         R-stats 
Requires:         R-CRAN-lvplot 
Requires:         R-CRAN-ggridges 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-ineq 
Requires:         R-CRAN-magrittr 
Requires:         R-utils 

%description
Provides tools for systematically exploring large quantities of temporal
data across different temporal granularities (deconstructions of time) by
visualizing probability distributions. 'gravitas' computes circular,
aperiodic, single-order-up or multiple-order-up granularities and advises
on which combinations of granularities to explore and through which
distribution plots.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/shiny-examples
%{rlibdir}/%{packname}/INDEX
