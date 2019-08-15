%global packname  brms
%global packver   2.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.9.0
Release:          1%{?dist}
Summary:          Bayesian Regression Models using 'Stan'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shinystan >= 2.4.0
BuildRequires:    R-CRAN-rstan >= 2.17.2
BuildRequires:    R-CRAN-loo >= 2.1.0
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-mgcv >= 1.8.13
BuildRequires:    R-CRAN-bayesplot >= 1.5.0
BuildRequires:    R-CRAN-rstantools >= 1.3.0
BuildRequires:    R-CRAN-glue >= 1.3.0
BuildRequires:    R-Matrix >= 1.1.1
BuildRequires:    R-CRAN-bridgesampling >= 0.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-backports 
Requires:         R-CRAN-shinystan >= 2.4.0
Requires:         R-CRAN-rstan >= 2.17.2
Requires:         R-CRAN-loo >= 2.1.0
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-mgcv >= 1.8.13
Requires:         R-CRAN-bayesplot >= 1.5.0
Requires:         R-CRAN-rstantools >= 1.3.0
Requires:         R-CRAN-glue >= 1.3.0
Requires:         R-Matrix >= 1.1.1
Requires:         R-CRAN-bridgesampling >= 0.3.0
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-methods 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-nleqslv 
Requires:         R-nlme 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-future 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-parallel 
Requires:         R-grDevices 
Requires:         R-CRAN-backports 

%description
Fit Bayesian generalized (non-)linear multivariate multilevel models using
'Stan' for full Bayesian inference. A wide range of distributions and link
functions are supported, allowing users to fit -- among others -- linear,
robust linear, count data, survival, response times, ordinal,
zero-inflated, hurdle, and even self-defined mixture models all in a
multilevel context. Further modeling options include non-linear and smooth
terms, auto-correlation structures, censored data, meta-analytic standard
errors, and quite a few more. In addition, all parameters of the response
distribution can be predicted in order to perform distributional
regression. Prior specifications are flexible and explicitly encourage
users to apply prior distributions that actually reflect their beliefs.
Model fit can easily be assessed and compared with posterior predictive
checks and leave-one-out cross-validation. References: Bürkner (2017)
<doi:10.18637/jss.v080.i01>; Carpenter et al. (2017)
<doi:10.18637/jss.v076.i01>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/chunks
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
