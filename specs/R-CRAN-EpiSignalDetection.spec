%global packname  EpiSignalDetection
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Signal Detection Analysis

License:          EUPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-knitr >= 1.20
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-pander 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-surveillance 
BuildRequires:    R-CRAN-ISOweek 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rmarkdown 
Requires:         R-CRAN-knitr >= 1.20
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-pander 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-surveillance 
Requires:         R-CRAN-ISOweek 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-rmarkdown 

%description
Exploring time series for signal detection. It is specifically designed to
detect possible outbreaks using infectious disease surveillance data at
the European Union / European Economic Area or country level. Automatic
detection tools used are presented in the paper "Monitoring count time
series in R: aberration detection in public health surveillance", by
Salmon et al. (2016) <doi:10.18637/jss.v070.i10>. The package includes: -
Signal Detection tool, an interactive 'shiny' application in which the
user can import external data and perform basic signal detection analyses;
- An automated report in HTML format, presenting the results of the time
series analysis in tables and graphs. This report can also be stratified
by population characteristics (see 'Population' variable). This project
was funded by the European Centre for Disease Prevention and Control.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/SignalDetectionApp
%doc %{rlibdir}/%{packname}/SignalDetectionReport_HTML
%doc %{rlibdir}/%{packname}/StratifiedSignalDetectionReport_HTML
%{rlibdir}/%{packname}/INDEX
