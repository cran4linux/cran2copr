%global packname  NonProbEst
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          3%{?dist}%{?buildtag}
Summary:          Estimation in Nonprobability Sampling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-sampling 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-sampling 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-glmnet 
Requires:         R-Matrix 

%description
Different inference procedures are proposed in the literature to correct
for selection bias that might be introduced with non-random selection
mechanisms. A class of methods to correct for selection bias is to apply a
statistical model to predict the units not in the sample (super-population
modeling). Other studies use calibration or Statistical Matching
(statistically match nonprobability and probability samples). To date, the
more relevant methods are weighting by Propensity Score Adjustment (PSA).
The Propensity Score Adjustment method was originally developed to
construct weights by estimating response probabilities and using them in
Horvitz–Thompson type estimators. This method is usually used by combining
a non-probability sample with a reference sample to construct propensity
models for the non-probability sample. Calibration can be used in a
posterior way to adding information of auxiliary variables. Propensity
scores in PSA are usually estimated using logistic regression models.
Machine learning classification algorithms can be used as alternatives for
logistic regression as a technique to estimate propensities. The package
'NonProbEst' implements some of these methods and thus provides a wide
options to work with data coming from a non-probabilistic sample.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
