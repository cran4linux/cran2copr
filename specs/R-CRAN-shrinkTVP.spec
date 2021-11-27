%global __brp_check_rpaths %{nil}
%global packname  shrinkTVP
%global packver   2.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Efficient Bayesian Inference for Time-Varying Parameter Models with Shrinkage

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-stochvol >= 3.0.3
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-GIGrvg 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppProgress 
Requires:         R-CRAN-stochvol >= 3.0.3
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-GIGrvg 
Requires:         R-CRAN-coda 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-zoo 

%description
Efficient Markov chain Monte Carlo (MCMC) algorithms for fully Bayesian
estimation of time-varying parameter models with shrinkage priors. Details
on the algorithms used are provided in Bitto and Frühwirth-Schnatter
(2019) <doi:10.1016/j.jeconom.2018.11.006> and Cadonna et al. (2020)
<doi:10.3390/econometrics8020020>. For details on the package, please see
Knaus et al. (2021) <doi:10.18637/jss.v100.i13>.

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
