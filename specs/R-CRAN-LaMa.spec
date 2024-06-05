%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LaMa
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Numerical Maximum Likelihood Estimation for Latent Markov Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-mgcv 

%description
The class of latent Markov models, including hidden Markov models, hidden
semi-Markov models, state space models, and point processes, is a very
popular and powerful framework for inference of time series driven by
latent processes. Furthermore, all these models can be fitted using direct
numerical maximum likelihood estimation using the so-called forward
algorithm as discussed in Zucchini et al. (2016) <doi:10.1201/b20790>.
However, due to their great flexibility, researchers using these models in
applied work often need to build highly customized models for which
standard software implementation is lacking, or the construction of such
models in said software is as complicated as writing fully tailored 'R'
code. While providing greater flexibility and control, the latter suffers
from slow estimation speeds that make custom solutions inconvenient. We
address the above issues in two ways. First, standard blocks of code,
common to all these model classes, are implemented as simple-to-use
functions that can be added like Lego blocks to an otherwise fully custom
likelihood function, making writing custom code much easier. Second, under
the hood, these functions are written in 'C++', allowing for 10-20 times
faster evaluation time, and thus drastically speeding up model estimation.
To aid in building fully custom likelihood functions, several vignettes
are included that show how to simulate data from and estimate all the
above model classes.

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
