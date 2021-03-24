%global packname  EdSurvey
%global packver   2.6.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.6.9
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of NCES Education Survey and Assessment Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-WeMix >= 3.1.6
BuildRequires:    R-CRAN-haven >= 2.2.0
BuildRequires:    R-CRAN-data.table >= 1.11.4
BuildRequires:    R-CRAN-lfactors >= 1.0.3
BuildRequires:    R-CRAN-LaF >= 0.7
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-glm2 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-NAEPprimer 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-wCorr 
BuildRequires:    R-CRAN-xtable 
Requires:         R-CRAN-WeMix >= 3.1.6
Requires:         R-CRAN-haven >= 2.2.0
Requires:         R-CRAN-data.table >= 1.11.4
Requires:         R-CRAN-lfactors >= 1.0.3
Requires:         R-CRAN-LaF >= 0.7
Requires:         R-CRAN-car 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-glm2 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-NAEPprimer 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-wCorr 
Requires:         R-CRAN-xtable 

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

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
