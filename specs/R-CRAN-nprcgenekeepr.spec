%global packname  nprcgenekeepr
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          3%{?dist}
Summary:          Genetic Tools for Colony Management

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-anytime 
BuildRequires:    R-CRAN-futile.logger 
BuildRequires:    R-CRAN-htmlTable 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-Rlabkey 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-WriteXLS 
Requires:         R-CRAN-anytime 
Requires:         R-CRAN-futile.logger 
Requires:         R-CRAN-htmlTable 
Requires:         R-CRAN-lubridate 
Requires:         R-Matrix 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-Rlabkey 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-stringi 
Requires:         R-utils 
Requires:         R-CRAN-WriteXLS 

%description
Provides genetic tools for colony management and is a derivation of the
work in Amanda Vinson and Michael J Raboin (2015)
<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4671785/> "A Practical
Approach for Designing Breeding Groups to Maximize Genetic Diversity in a
Large Colony of Captive Rhesus Macaques ('Macaca' 'mulatto')". It provides
a 'Shiny' application with an exposed API. The application supports five
groups of functions: (1) Quality control of studbooks contained in text
files or 'Excel' workbooks and of pedigrees within 'LabKey' Electronic
Health Records (EHR); (2) Creation of pedigrees from a list of animals
using the 'LabKey' EHR integration; (3) Creation and display of an age by
sex pyramid plot of the living animals within the designated pedigree; (4)
Generation of genetic value analysis reports; and (5) Creation of
potential breeding groups with and without proscribed sex ratios and
defined maximum kinships.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/_pkgdown.yml
%doc %{rlibdir}/%{packname}/application
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/testdata
%{rlibdir}/%{packname}/INDEX
