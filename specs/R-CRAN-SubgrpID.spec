%global packname  SubgrpID
%global packver   0.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.11
Release:          1%{?dist}
Summary:          Patient Subgroup Identification for Clinical Drug Development

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.1.0
Requires:         R-core >= 2.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-AIM 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-Matrix 
BuildRequires:    R-rpart 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-glmnet 
Requires:         R-CRAN-AIM 
Requires:         R-survival 
Requires:         R-CRAN-ggplot2 
Requires:         R-Matrix 
Requires:         R-rpart 
Requires:         R-stats 
Requires:         R-CRAN-glmnet 

%description
Function Wrapper contains four algorithms for developing threshold-based
multivariate (prognostic/predictive) biomarker signatures via
bootstrapping and aggregating of thresholds from trees, Monte-Carlo
variations of the Adaptive Indexing method and Patient Rule Induction
Method. Variable selection is automatically built-in to these algorithms.
Final signatures are returned with interaction plots for predictive
signatures. Cross-validation performance evaluation and testing dataset
results are also output.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
