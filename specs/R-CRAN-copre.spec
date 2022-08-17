%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  copre
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Nonparametric Martingale Posterior Sampling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-dirichletprocess 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-dirichletprocess 

%description
Performs Bayesian nonparametric density estimation using Martingale
posterior distributions and including the Copula Resampling (CopRe)
algorithm. Also included are a Gibbs sampler for the marginal Mixture of
Dirichlet Process (MDP) model and an extension to include full uncertainty
quantification via a new Polya completion algorithm for the MDP. The CopRe
and Polya samplers generate random nonparametric distributions as output,
leading to complete nonparametric inference on posterior summaries.
Routines for calculating arbitrary functionals from the sampled
distributions are included as well as an important algorithm for finding
the number and location of modes, which can then be used to estimate the
clusters in the data using, for example, k-means. Implements work
developed in Moya B., Walker S. G. (2022) <doi:10.48550/arxiv.2206.08418>,
Fong, E., Holmes, C., Walker, S. G. (2021)
<doi:10.48550/arxiv.2103.15671>, and Escobar M. D., West, M. (1995)
<doi:10.1080/01621459.1995.10476550>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
