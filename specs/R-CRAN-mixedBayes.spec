%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mixedBayes
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Longitudinal Regularized Quantile Mixed Model

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 

%description
In longitudinal studies, the same subjects are measured repeatedly over
time, leading to correlations among the repeated measurements. Properly
accounting for the intra-cluster correlations in the presence of data
heterogeneity and long tailed distributions of the disease phenotype is
challenging, especially in the context of high dimensional regressions.
Here, we aim at developing novel Bayesian regularized quantile mixed
effect models to tackle these challenges. We have proposed a Bayesian
variable selection in the mixed effect models for longitudinal genomics
studies. To dissect important gene - environment interactions, our model
can simultaneously identify important main and interaction effects on the
individual and group level, which have been facilitated by imposing the
spike- and -slab priors through Laplacian shrinkage in the Bayesian
quantile hierarchical models. The within - subject dependence among data
can be accommodated by incorporating the random effects. An efficient
Gibbs sampler has been developed to facilitate fast computation. The
Markov chain Monte Carlo algorithms of the proposed and alternative
methods are efficiently implemented in 'C++'. The development of this
software package and the associated statistical methods have been
partially supported by an Innovative Research Award from Johnson Cancer
Research Center, Kansas State University.

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
