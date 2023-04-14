%global __brp_check_rpaths %{nil}
%global packname  CustomerScoringMetrics
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Evaluation Metrics for Customer Scoring Models Depending onBinary Classifiers

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Functions for evaluating and visualizing predictive model performance
(specifically: binary classifiers) in the field of customer scoring. These
metrics include lift, lift index, gain percentage, top-decile lift,
F1-score, expected misclassification cost and absolute misclassification
cost. See Berry & Linoff (2004, ISBN:0-471-47064-3), Witten and Frank
(2005, 0-12-088407-0) and Blattberg, Kim & Neslin (2008,
ISBN:978–0–387–72578–9) for details. Visualization functions are included
for lift charts and gain percentage charts. All metrics that require class
predictions offer the possibility to dynamically determine cutoff values
for transforming real-valued probability predictions into class
predictions.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
