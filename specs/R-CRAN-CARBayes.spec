%global packname  CARBayes
%global packver   5.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.1.2
Release:          1%{?dist}
Summary:          Spatial Generalised Linear Mixed Models for Areal Unit Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.5
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-CARBayesdata 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp >= 0.11.5
Requires:         R-MASS 
Requires:         R-CRAN-CARBayesdata 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-spam 
Requires:         R-CRAN-spdep 
Requires:         R-stats 
Requires:         R-CRAN-truncnorm 
Requires:         R-utils 

%description
Implements a class of univariate and multivariate spatial generalised
linear mixed models for areal unit data, with inference in a Bayesian
setting using Markov chain Monte Carlo (MCMC) simulation. The response
variable can be binomial, Gaussian, multinomial, Poisson or zero-inflated
Poisson (ZIP), and spatial autocorrelation is modelled by a set of random
effects that are assigned a conditional autoregressive (CAR) prior
distribution. A number of different models are available for univariate
spatial data, including models with no random effects as well as random
effects modelled by different types of CAR prior, including the BYM model
(Besag et al. (1991) <doi:10.1007/BF00116466>), the Leroux model (Leroux
et al. (2000) <doi:10.1007/978-1-4612-1284-3_4>) and the localised model
(Lee et al. (2015) <doi:10.1002/env.2348>). Additionally, a multivariate
CAR (MCAR) model for multivariate spatial data is available, as is a
two-level hierarchical model for modelling data relating to individuals
within areas. Full details are given in the vignette accompanying this
package. The initial creation of this package was supported by the
Economic and Social Research Council (ESRC) grant RES-000-22-4256, and
on-going development has been supported by the Engineering and Physical
Science Research Council (EPSRC) grant EP/J017442/1, ESRC grant
ES/K006460/1, Innovate UK / Natural Environment Research Council (NERC)
grant NE/N007352/1 and the TB Alliance.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
