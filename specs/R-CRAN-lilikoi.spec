%global packname  lilikoi
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Metabolomics Personalized Pathway Analysis Tool

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-hash 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-infotheo 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-pamr 
BuildRequires:    R-CRAN-R.oo 
BuildRequires:    R-CRAN-princurve 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-RWeka 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-hash 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-infotheo 
Requires:         R-Matrix 
Requires:         R-CRAN-pamr 
Requires:         R-CRAN-R.oo 
Requires:         R-CRAN-princurve 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-RWeka 
Requires:         R-CRAN-stringr 

%description
Computes the pathway deregulation score for a given set of metabolites,
selects the pathways with the highest mutual information and then uses
them to build a classifier. F. Alakwaa, S. Huang, and L. Garmire (2018)
<doi:10.1101/283408>.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
