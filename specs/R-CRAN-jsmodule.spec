%global packname  jsmodule
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}
Summary:          'RStudio' Addins and 'Shiny' Modules for Medical Research

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-jstable 
BuildRequires:    R-CRAN-labelled 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-epiDisplay 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-shinycustomloader 
BuildRequires:    R-CRAN-MatchIt 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-tableone 
BuildRequires:    R-CRAN-jskm 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-geepack 
BuildRequires:    R-CRAN-maxstat 
BuildRequires:    R-CRAN-survC1 
BuildRequires:    R-CRAN-survIDINRI 
BuildRequires:    R-CRAN-timeROC 
BuildRequires:    R-CRAN-devEMF 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-see 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-jstable 
Requires:         R-CRAN-labelled 
Requires:         R-methods 
Requires:         R-CRAN-epiDisplay 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-shinycustomloader 
Requires:         R-CRAN-MatchIt 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-tableone 
Requires:         R-CRAN-jskm 
Requires:         R-survival 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-geepack 
Requires:         R-CRAN-maxstat 
Requires:         R-CRAN-survC1 
Requires:         R-CRAN-survIDINRI 
Requires:         R-CRAN-timeROC 
Requires:         R-CRAN-devEMF 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-see 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-RColorBrewer 

%description
'RStudio' addins and 'Shiny' modules for descriptive statistics,
regression and survival analysis.

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
%doc %{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/INDEX
