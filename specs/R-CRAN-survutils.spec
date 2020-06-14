%global packname  survutils
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          2%{?dist}
Summary:          Utility Functions for Survival Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-survival >= 2.38.3
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-survC1 >= 1.0.2
BuildRequires:    R-CRAN-ggplot2 >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.4.3
BuildRequires:    R-CRAN-broom >= 0.3.7
BuildRequires:    R-CRAN-lazyeval >= 0.2.0
BuildRequires:    R-CRAN-purrr >= 0.1.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-glue 
Requires:         R-survival >= 2.38.3
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-survC1 >= 1.0.2
Requires:         R-CRAN-ggplot2 >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.4.3
Requires:         R-CRAN-broom >= 0.3.7
Requires:         R-CRAN-lazyeval >= 0.2.0
Requires:         R-CRAN-purrr >= 0.1.0
Requires:         R-stats 
Requires:         R-CRAN-glue 

%description
Functional programming principles to iteratively run Cox regression and
plot its results. The results are reported in tidy data frames. Additional
utility functions are available for working with other aspects of survival
analysis such as survival curves, C-statistics, etc.

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
%{rlibdir}/%{packname}/INDEX
