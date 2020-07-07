%global packname  icd
%global packver   4.0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0.9
Release:          3%{?dist}
Summary:          Comorbidity Calculations and Tools for ICD-9 and ICD-10 Codes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.12.3
Requires:         R-methods 

%description
Calculate comorbidities, medical risk scores, and work very quickly and
precisely with ICD-9 and ICD-10 codes. This package enables a work flow
from raw tables of ICD codes in hospital databases to comorbidities. ICD-9
and ICD-10 comorbidity mappings from Quan (Deyo and Elixhauser versions),
Elixhauser and AHRQ included. Common ambiguities and code formats are
handled. Comorbidity computation includes Hierarchical Condition Codes,
and an implementation of AHRQ Clinical Classifications. Risk scores
include those of Charlson and van Walraven.  US Clinical Modification,
Word Health Organization, Belgian and French ICD-10 codes are supported,
most of which are downloaded on demand.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/_pkgdown.yml
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/m4
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
%doc %{rlibdir}/%{packname}/COPYING
