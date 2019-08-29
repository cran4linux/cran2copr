%global packname  EBPRS
%global packver   1.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.5
Release:          1%{?dist}
Summary:          Derive Polygenic Risk Score Based on Emprical Bayes Theory

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-methods 
Requires:         R-CRAN-ROCR 
Requires:         R-CRAN-data.table 
Requires:         R-methods 

%description
EB-PRS is a novel method that leverages information for effect sizes
across all the markers to improve the prediction accuracy.  No parameter
tuning is needed in the method, and no external information is needed.
This R-package provides the calculation of polygenic risk scores from the
given training summary statistics and testing data. We can use EB-PRS to
extract main information, estimate Empirical Bayes parameters, derive
polygenic risk scores for each individual in testing data, and evaluate
the PRS according to AUC and predictive r2.

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
%{rlibdir}/%{packname}/INDEX
