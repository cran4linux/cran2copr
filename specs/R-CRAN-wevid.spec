%global __brp_check_rpaths %{nil}
%global packname  wevid
%global packver   0.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.2
Release:          3%{?dist}%{?buildtag}
Summary:          Quantifying Performance of a Binary Classifier Through Weight ofEvidence

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-pROC >= 1.9
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-pROC >= 1.9
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-zoo 

%description
The distributions of the weight of evidence (log Bayes factor) favouring
case over noncase status in a test dataset (or test folds generated by
cross-validation) can be used to quantify the performance of a diagnostic
test (McKeigue (2019), <doi:10.1177/0962280218776989>). The package can be
used with any test dataset on which you have observed case-control status
and have computed prior and posterior probabilities of case status using a
model learned on a training dataset. To quantify how the predictor will
behave as a risk stratifier, the quantiles of the distributions of weight
of evidence in cases and controls can be calculated and plotted.

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
