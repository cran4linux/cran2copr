%global packname  spCP
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}
Summary:          Spatially Varying Change Points

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-msm >= 1.0.0
BuildRequires:    R-CRAN-mvtnorm >= 1.0.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.7.500.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.9
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-msm >= 1.0.0
Requires:         R-CRAN-mvtnorm >= 1.0.0
Requires:         R-CRAN-Rcpp >= 0.12.9
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 

%description
Implements a spatially varying change point model with unique intercepts,
slopes, variance intercepts and slopes, and change points at each
location. Inference is within the Bayesian setting using Markov chain
Monte Carlo (MCMC). The response variable can be modeled as Gaussian (no
nugget), probit or Tobit link and the five spatially varying parameter are
modeled jointly using a multivariate conditional autoregressive (MCAR)
prior. The MCAR is a unique process that allows for a dissimilarity metric
to dictate the local spatial dependencies. Full details of the package can
be found in the accompanying vignette. Furthermore, the details of the
package can be found in the corresponding paper on arXiv by Berchuck et al
(2018): "A spatially varying change points model for monitoring glaucoma
progression using visual field data", <arXiv:1811.11038>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
