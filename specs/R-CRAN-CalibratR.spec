%global packname  CalibratR
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}
Summary:          Mapping ML Scores to Calibrated Predictions

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-reshape2 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 
Requires:         R-stats 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-doParallel 

%description
Transforms your uncalibrated Machine Learning scores to well-calibrated
prediction estimates that can be interpreted as probability estimates. The
implemented BBQ (Bayes Binning in Quantiles) model is taken from Naeini
(2015, ISBN:0-262-51129-0). Please cite this paper: Schwarz J and Heider
D, Bioinformatics 2019, 35(14):2458-2465.

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
%{rlibdir}/%{packname}/INDEX
