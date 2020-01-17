%global packname  revdbayes
%global packver   1.3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.6
Release:          1%{?dist}
Summary:          Ratio-of-Uniforms Sampling for Bayesian Extreme Value Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-rust >= 1.2.2
BuildRequires:    R-CRAN-bayesplot >= 1.1.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.10
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-rust >= 1.2.2
Requires:         R-CRAN-bayesplot >= 1.1.0
Requires:         R-graphics 
Requires:         R-CRAN-Rcpp >= 0.12.10
Requires:         R-stats 
Requires:         R-utils 

%description
Provides functions for the Bayesian analysis of extreme value models.  The
'rust' package <https://cran.r-project.org/package=rust> is used to
simulate a random sample from the required posterior distribution. The
functionality of 'revdbayes' is similar to the 'evdbayes' package
<https://cran.r-project.org/package=evdbayes>, which uses Markov Chain
Monte Carlo ('MCMC') methods for posterior simulation.  Also provided are
functions for making inferences about the extremal index, using the K-gaps
model of Suveges and Davison (2010) <doi:10.1214/09-AOAS292>. Also
provided are d,p,q,r functions for the Generalised Extreme Value ('GEV')
and Generalised Pareto ('GP') distributions that deal appropriately with
cases where the shape parameter is very close to zero.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
