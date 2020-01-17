%global packname  EdSurvey
%global packver   2.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.0
Release:          1%{?dist}
Summary:          Analysis of NCES Education Survey and Assessment Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-WeMix >= 3.1.3
BuildRequires:    R-CRAN-data.table >= 1.11.4
BuildRequires:    R-CRAN-lfactors >= 1.0.3
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-glm2 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-LaF 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-NAEPprimer 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-wCorr 
BuildRequires:    R-CRAN-quantreg 
Requires:         R-CRAN-WeMix >= 3.1.3
Requires:         R-CRAN-data.table >= 1.11.4
Requires:         R-CRAN-lfactors >= 1.0.3
Requires:         R-CRAN-car 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-glm2 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-LaF 
Requires:         R-CRAN-lme4 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-NAEPprimer 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-wCorr 
Requires:         R-CRAN-quantreg 

%description
Read in and analyze functions for education survey and assessment data
from the National Center for Education Statistics (NCES)
<https://nces.ed.gov/>, including National Assessment of Educational
Progress (NAEP) data <https://nces.ed.gov/nationsreportcard/> and data
from the International Assessment Database: Organisation for Economic
Co-operation and Development (OECD) <https://www.oecd.org/>, including
Programme for International Student Assessment (PISA), Teaching and
Learning International Survey (TALIS), Programme for the International
Assessment of Adult Competencies (PIAAC), and International Association
for the Evaluation of Educational Achievement (IEA) <https://www.iea.nl/>,
including Trends in International Mathematics and Science Study (TIMSS),
TIMSS Advanced, Progress in International Reading Literacy Study (PIRLS),
International Civic and Citizenship Study (ICCS), International Computer
and Information Literacy Study (ICILS), and Civic Education Study (CivEd).

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/linkingErrors
%doc %{rlibdir}/%{packname}/mapproj
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/suggestWeights
%{rlibdir}/%{packname}/INDEX
