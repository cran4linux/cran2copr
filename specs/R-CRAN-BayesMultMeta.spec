%global __brp_check_rpaths %{nil}
%global packname  BayesMultMeta
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Multivariate Meta-Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-Rdpack 

%description
Objective Bayesian inference procedures for the parameters of the
multivariate random effects model with application to multivariate
meta-analysis. The posterior for the model parameters, namely the overall
mean vector and the between-study covariance matrix, are assessed by
constructing Markov chains based on the Metropolis-Hastings algorithms as
developed in Bodnar and Bodnar (2021) (<arXiv:2104.02105>). The
Metropolis-Hastings algorithm is designed under the assumption of the
normal distribution and the t-distribution when the Berger and Bernardo
reference prior and the Jeffreys prior are assigned to the model
parameters. Convergence properties of the generated Markov chains are
investigated by the rank plots and the split hat-R estimate based on the
rank normalization, which are proposed in Vehtari et al. (2021)
(<DOI:10.1214/20-BA1221>).

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
