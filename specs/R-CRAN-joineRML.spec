%global packname  joineRML
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          1%{?dist}
Summary:          Joint Modelling of Multivariate Longitudinal Data andTime-to-Event Outcomes

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-lme4 >= 1.1.8
BuildRequires:    R-CRAN-Rcpp >= 0.12.7
BuildRequires:    R-nlme 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-cobs 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-lme4 >= 1.1.8
Requires:         R-CRAN-Rcpp >= 0.12.7
Requires:         R-nlme 
Requires:         R-survival 
Requires:         R-CRAN-cobs 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-CRAN-mvtnorm 
Requires:         R-parallel 
Requires:         R-CRAN-randtoolbox 
Requires:         R-stats 
Requires:         R-utils 

%description
Fits the joint model proposed by Henderson and colleagues (2000)
<doi:10.1093/biostatistics/1.4.465>, but extended to the case of multiple
continuous longitudinal measures. The time-to-event data is modelled using
a Cox proportional hazards regression model with time-varying covariates.
The multiple longitudinal outcomes are modelled using a multivariate
version of the Laird and Ware linear mixed model. The association is
captured by a multivariate latent Gaussian process. The model is estimated
using a Monte Carlo Expectation Maximization algorithm. This project is
funded by the Medical Research Council (Grant number MR/M013227/1).

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
