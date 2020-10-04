%global packname  mccf1
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Creates the MCC-F1 Curve and Calculates the MCC-F1 Metric andthe Best Threshold

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.3
Requires:         R-core >= 3.3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ROCR 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ROCR 

%description
The MCC-F1 analysis is a method to evaluate the performance of binary
classifications. The MCC-F1 curve is more reliable than the Receiver
Operating Characteristic (ROC) curve and the Precision-Recall (PR)curve
under imbalanced ground truth. The MCC-F1 analysis also provides the
MCC-F1 metric that integrates classifier performance over varying
thresholds, and the best threshold of binary classification.

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
