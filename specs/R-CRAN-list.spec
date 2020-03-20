%global packname  list
%global packver   9.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          9.2
Release:          1%{?dist}
Summary:          Statistical Methods for the Item Count Technique and ListExperiment

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-MASS >= 7.3.40
BuildRequires:    R-CRAN-gamlss.dist >= 4.3.4
BuildRequires:    R-CRAN-sandwich >= 2.3.3
BuildRequires:    R-CRAN-corpcor >= 1.6.7
BuildRequires:    R-CRAN-magic >= 1.5.6
BuildRequires:    R-CRAN-quadprog >= 1.5.5
BuildRequires:    R-CRAN-mvtnorm >= 1.0.2
BuildRequires:    R-CRAN-VGAM >= 0.9.8
BuildRequires:    R-CRAN-coda >= 0.17.1
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-arm 
Requires:         R-MASS >= 7.3.40
Requires:         R-CRAN-gamlss.dist >= 4.3.4
Requires:         R-CRAN-sandwich >= 2.3.3
Requires:         R-CRAN-corpcor >= 1.6.7
Requires:         R-CRAN-magic >= 1.5.6
Requires:         R-CRAN-quadprog >= 1.5.5
Requires:         R-CRAN-mvtnorm >= 1.0.2
Requires:         R-CRAN-VGAM >= 0.9.8
Requires:         R-CRAN-coda >= 0.17.1
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-arm 

%description
Allows researchers to conduct multivariate statistical analyses of survey
data with list experiments. This survey methodology is also known as the
item count technique or the unmatched count technique and is an
alternative to the commonly used randomized response method. The package
implements the methods developed by Imai (2011)
<doi:10.1198/jasa.2011.ap10415>, Blair and Imai (2012)
<doi:10.1093/pan/mpr048>, Blair, Imai, and Lyall (2013)
<doi:10.1111/ajps.12086>, Imai, Park, and Greene (2014)
<doi:10.1093/pan/mpu017>, Aronow, Coppock, Crawford, and Green (2015)
<doi:10.1093/jssam/smu023>, Chou, Imai, and Rosenfeld (2017)
<doi:10.1177/0049124117729711>, and Blair, Chou, and Imai (2018)
<https://imai.fas.harvard.edu/research/files/listerror.pdf>. This includes
a Bayesian MCMC implementation of regression for the standard and multiple
sensitive item list experiment designs and a random effects setup, a
Bayesian MCMC hierarchical regression model with up to three hierarchical
groups, the combined list experiment and endorsement experiment regression
model, a joint model of the list experiment that enables the analysis of
the list experiment as a predictor in outcome regression models, a method
for combining list experiments with direct questions, and methods for
diagnosing and adjusting for response error. In addition, the package
implements the statistical test that is designed to detect certain
failures of list experiments, and a placebo test for the list experiment
using data from direct questions.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
