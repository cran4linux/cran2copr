%global packname  geneHummus
%global packver   1.0.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.11
Release:          2%{?dist}
Summary:          A Pipeline to Define Gene Families in Legumes and Beyond

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 3.3
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-httr >= 1.4.0
BuildRequires:    R-CRAN-rentrez >= 1.2.1
BuildRequires:    R-CRAN-dplyr >= 0.8.0.1
BuildRequires:    R-utils 
Requires:         R-CRAN-curl >= 3.3
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-httr >= 1.4.0
Requires:         R-CRAN-rentrez >= 1.2.1
Requires:         R-CRAN-dplyr >= 0.8.0.1
Requires:         R-utils 

%description
A pipeline with high specificity and sensitivity in extracting proteins
from the RefSeq database (National Center for Biotechnology Information).
Manual identification of gene families is highly time-consuming and
laborious, requiring an iterative process of manual and computational
analysis to identify members of a given family. The pipelines implements
an automatic approach for the identification of gene families based on the
conserved domains that specifically define that family. See Die et al.
(2018) <doi:10.1101/436659> for more information and examples.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
