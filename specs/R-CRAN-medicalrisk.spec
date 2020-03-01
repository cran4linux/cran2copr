%global packname  medicalrisk
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          Medical Risk and Comorbidity Tools for ICD-9-CM Data

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plyr >= 1.5
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-hash 
Requires:         R-CRAN-plyr >= 1.5
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-hash 

%description
Generates risk estimates and comorbidity flags from ICD-9-CM codes
available in administrative medical datasets. The package supports the
Charlson Comorbidity Index, the Elixhauser Comorbidity classification, the
Revised Cardiac Risk Index, and the Risk Stratification Index.  Methods
are table-based, fast, and use the 'plyr' package, so parallelization is
possible for large jobs. Also includes a sample of real ICD-9 data for 100
patients from a publicly available dataset.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/sql
%{rlibdir}/%{packname}/INDEX
