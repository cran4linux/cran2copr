%global __brp_check_rpaths %{nil}
%global packname  bestSDP
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Burden Estimate of Common Communicable Diseases in Settlementsof Displaced Populations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-stringr 

%description
Provides a practical tool for estimating the burden of common communicable
diseases in settlements of displaced populations. An online version of the
tool can be found at <http://who-refugee-bod.ecdf.ed.ac.uk/shiny/app/>.
Estimates of burden of disease aim to synthesize data about cause-specific
morbidity and mortality through a systematic approach that enables
evidence-based decisions and comparisons across settings. The focus of
this tool is on four acute communicable diseases and syndromes, including
Acute respiratory infections, Acute diarrheal diseases, Acute jaundice
syndrome and Acute febrile illnesses.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/shinyapps
%{rlibdir}/%{packname}/INDEX
