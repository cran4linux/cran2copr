%global packname  PAutilities
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          Streamline Physical Activity Research

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-matchingMarkets >= 1.0.1
BuildRequires:    R-CRAN-dplyr >= 0.7
BuildRequires:    R-CRAN-clues >= 0.6.1
BuildRequires:    R-CRAN-rlang >= 0.3.1
BuildRequires:    R-CRAN-lazyeval >= 0.2
BuildRequires:    R-CRAN-equivalence 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 2.2
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-matchingMarkets >= 1.0.1
Requires:         R-CRAN-dplyr >= 0.7
Requires:         R-CRAN-clues >= 0.6.1
Requires:         R-CRAN-rlang >= 0.3.1
Requires:         R-CRAN-lazyeval >= 0.2
Requires:         R-CRAN-equivalence 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-utils 

%description
A collection of utilities that are useful for a broad range of tasks that
are common in physical activity research, including the following:
creation of Bland-Altman plots, formatted descriptive statistics,
metabolic calculations (e.g. basal metabolic rate predictions) and
conversions, demographic calculations (age and age-for-body-mass-index
percentile), bout analysis of moderate-to-vigorous intensity physical
activity, and analysis of bout detection algorithm performance.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
