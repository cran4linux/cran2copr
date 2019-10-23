%global packname  breathtestcore
%global packver   0.4.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.6
Release:          1%{?dist}
Summary:          Core Functions to Read and Fit 13c Time Series from Breath Tests

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc
BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 1.4.0
BuildRequires:    R-nlme 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggfittext 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-tibble >= 1.4.0
Requires:         R-nlme 
Requires:         R-MASS 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-methods 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggfittext 
Requires:         R-CRAN-signal 
Requires:         R-utils 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-xml2 

%description
Reads several formats of 13C data (IRIS/Wagner, BreathID) and CSV. Creates
artificial sample data for testing. Fits Maes/Ghoos, Bluck-Coward
self-correcting formula using 'nls', 'nlme'. Methods to fit breath test
curves with Bayesian Stan methods are refactored to package
'breathteststan'. For a Shiny GUI, see package 'dmenne/breathtestshiny' on
github.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
