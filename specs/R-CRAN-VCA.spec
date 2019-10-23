%global packname  VCA
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}
Summary:          Variance Component Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-lme4 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-numDeriv 

%description
ANOVA and REML estimation of linear mixed models is implemented, once
following Searle et al. (1991, ANOVA for unbalanced data), once making use
of the 'lme4' package. The primary objective of this package is to perform
a variance component analysis (VCA) according to CLSI EP05-A3 guideline
"Evaluation of Precision of Quantitative Measurement Procedures" (2014).
There are plotting methods for visualization of an experimental design,
plotting random effects and residuals. For ANOVA type estimation two
methods for computing ANOVA mean squares are implemented (SWEEP and
quadratic forms). The covariance matrix of variance components can be
derived, which is used in estimating confidence intervals. Linear
hypotheses of fixed effects and LS means can be computed. LS means can be
computed at specific values of covariables and with custom weighting
schemes for factor variables. See ?VCA for a more comprehensive
description of the features.

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
%doc %{rlibdir}/%{packname}/ChangeLog.txt
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/UnitTests
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
