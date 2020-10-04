%global packname  sensitivityCalibration
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          A Calibrated Sensitivity Analysis for Matched ObservationalStudies

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-relaimpo 
BuildRequires:    R-CRAN-splitstackshape 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-plotly 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-relaimpo 
Requires:         R-CRAN-splitstackshape 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-plotly 

%description
Implements the calibrated sensitivity analysis approach for matched
observational studies. Our sensitivity analysis framework views matched
sets as drawn from a super-population. The unmeasured confounder is
modeled as a random variable. We combine matching and model-based
covariate-adjustment methods to estimate the treatment effect. The
hypothesized unmeasured confounder enters the picture as a missing
covariate. We adopt a state-of-art Expectation Maximization (EM) algorithm
to handle this missing covariate problem in generalized linear models
(GLMs). As our method also estimates the effect of each observed covariate
on the outcome and treatment assignment, we are able to calibrate the
unmeasured confounder to observed covariates. Zhang, B., Small, D. S.
(2018). <arXiv:1812.00215>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
