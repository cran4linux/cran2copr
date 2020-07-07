%global packname  fabMix
%global packver   5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.0
Release:          3%{?dist}
Summary:          Overfitting Bayesian Mixtures of Factor Analyzers withParsimonious Covariance and Unknown Number of Components

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.17
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-label.switching 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.17
Requires:         R-MASS 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-label.switching 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-ggplot2 

%description
Model-based clustering of multivariate continuous data using Bayesian
mixtures of factor analyzers (Papastamoulis (2019)
<DOI:10.1007/s11222-019-09891-z> (2018) <DOI:10.1016/j.csda.2018.03.007>).
The number of clusters is estimated using overfitting mixture models
(Rousseau and Mengersen (2011) <DOI:10.1111/j.1467-9868.2011.00781.x>):
suitable prior assumptions ensure that asymptotically the extra components
will have zero posterior weight, therefore, the inference is based on the
``alive'' components. A Gibbs sampler is implemented in order to
(approximately) sample from the posterior distribution of the overfitting
mixture. A prior parallel tempering scheme is also available, which allows
to run multiple parallel chains with different prior distributions on the
mixture weights. These chains run in parallel and can swap states using a
Metropolis-Hastings move. Eight different parameterizations give rise to
parsimonious representations of the covariance per cluster (following Mc
Nicholas and Murphy (2008) <DOI:10.1007/s11222-008-9056-0>). The model
parameterization and number of factors is selected according to the
Bayesian Information Criterion. Identifiability issues related to label
switching are dealt by post-processing the simulated output with the
Equivalence Classes Representatives algorithm (Papastamoulis and
Iliopoulos (2010) <https://www.jstor.org/stable/25703571>, Papastamoulis
(2016) <DOI:10.18637/jss.v069.c01>).

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
