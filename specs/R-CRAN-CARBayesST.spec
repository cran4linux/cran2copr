%global packname  CARBayesST
%global packver   3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1
Release:          2%{?dist}
Summary:          Spatio-Temporal Generalised Linear Mixed Models for Areal UnitData

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.5
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-CARBayesdata 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-truncdist 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp >= 0.11.5
Requires:         R-MASS 
Requires:         R-CRAN-CARBayesdata 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-spam 
Requires:         R-CRAN-spdep 
Requires:         R-stats 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-truncdist 
Requires:         R-CRAN-truncnorm 
Requires:         R-utils 

%description
Implements a class of spatio-temporal generalised linear mixed models for
areal unit data, with inference in a Bayesian setting using Markov chain
Monte Carlo (MCMC) simulation. The response variable can be binomial,
Gaussian, or Poisson, but for some models only the binomial and Poisson
data likelihoods are available. The spatio-temporal autocorrelation is
modelled by random effects, which are assigned conditional autoregressive
(CAR) style prior distributions. A number of different random effects
structures are available, including models similar to Bernardinelli et al.
(1995) <doi:10.1002/sim.4780142112>, Rushworth et al. (2014)
<doi:10.1016/j.sste.2014.05.001> and Lee et al. (2016)
<doi:10.1214/16-AOAS941>. Full details are given in the vignette
accompanying this package. The creation of this package was supported by
the Engineering and Physical Sciences Research Council (EPSRC) grant
EP/J017442/1 and the Medical Research Council (MRC) grant MR/L022184/1.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
