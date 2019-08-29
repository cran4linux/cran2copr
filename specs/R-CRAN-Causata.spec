%global packname  Causata
%global packver   4.2-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.2.0
Release:          1%{?dist}
Summary:          Analysis utilities for binary classification and Causata users.

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildArch:        noarch
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-RMySQL 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-RMySQL 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-yaml 
Requires:         R-boot 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-ggplot2 

%description
The Causata package provides utilities for extracting data from the
Causata application, training binary classification models, and exporting
models as PMML for scoring.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
