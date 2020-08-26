%global packname  MetabolicSurv
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Biomarker Validation Approach for Classification andPredicting Survival Using Metabolomics Signature

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack >= 0.11.0
BuildRequires:    R-CRAN-superpc 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-survminer 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-Rdpack >= 0.11.0
Requires:         R-CRAN-superpc 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-survminer 
Requires:         R-survival 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-pls 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-ggplot2 

%description
An approach to identifies metabolic biomarker signature for metabolic data
by discovering predictive metabolite for predicting survival and
classifying patients into risk groups. Classifiers are constructed as a
linear combination of predictive/important metabolites, prognostic factors
and treatment effects if necessary. Several methods were implemented to
reduce the metabolomics matrix such as the principle component analysis of
Wold Svante et al. (1987) <doi:10.1016/0169-7439(87)80084-9> , the LASSO
method by Robert Tibshirani (1998)
<doi:10.1002/(SICI)1097-0258(19970228)16:4%3C385::AID-SIM380%3E3.0.CO;2-3>,
the elastic net approach by Hui Zou and Trevor Hastie (2005)
<doi:10.1111/j.1467-9868.2005.00503.x>. Sensitivity analysis on the
quantile used for the classification can also be accessed to check the
deviation of the classification group based on the quantile specified.
Large scale cross validation can be performed in order to investigate the
mostly selected predictive metabolites and for internal validation. During
the evaluation process, validation is accessed using the hazard ratios
(HR) distribution of the test set and inference is mainly based on
resampling and permutations technique.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
