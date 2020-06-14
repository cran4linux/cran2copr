%global packname  cvAUC
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          2%{?dist}
Summary:          Cross-Validated Area Under the ROC Curve Confidence Intervals

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-ROCR 
Requires:         R-CRAN-data.table 

%description
This package contains various tools for working with and evaluating
cross-validated area under the ROC curve (AUC) estimators.  The primary
functions of the package are ci.cvAUC and ci.pooled.cvAUC, which report
cross-validated AUC and compute confidence intervals for cross-validated
AUC estimates based on influence curves for i.i.d. and pooled repeated
measures data, respectively.  One benefit to using influence curve based
confidence intervals is that they require much less computation time than
bootstrapping methods.  The utility functions, AUC and cvAUC, are simple
wrappers for functions from the ROCR package.

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
%{rlibdir}/%{packname}/INDEX
