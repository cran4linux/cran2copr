%global packname  rpubchem
%global packver   1.5.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.10
Release:          2%{?dist}
Summary:          An Interface to the PubChem Collection

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0.0
Requires:         R-core >= 2.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-RJSONIO 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-itertools 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-fingerprint 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-methods 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-car 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-RJSONIO 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-itertools 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-fingerprint 
Requires:         R-CRAN-base64enc 
Requires:         R-methods 

%description
Access PubChem data (compounds, substance, assays) using R. Structural
information is provided in the form of SMILES strings. It currently only
provides access to a subset of the precalculated data stored by PubChem.
Bio-assay data can be accessed to obtain descriptions as well as the
actual data. It is also possible to search for assay ID's by keyword.

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
%doc %{rlibdir}/%{packname}/pugxml
%{rlibdir}/%{packname}/INDEX
