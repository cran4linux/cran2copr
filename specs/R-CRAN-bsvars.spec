%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bsvars
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Estimation of Structural Vector Autoregressive Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-RcppProgress >= 0.1
BuildRequires:    R-CRAN-RcppTN 
BuildRequires:    R-CRAN-GIGrvg 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-RcppProgress >= 0.1
Requires:         R-CRAN-RcppTN 
Requires:         R-CRAN-GIGrvg 
Requires:         R-CRAN-R6 

%description
Efficient algorithms for Bayesian estimation of Structural Vector
Autoregressive (SVAR) models via Markov chain Monte Carlo methods. A wide
range of SVAR models is considered, including homo- and heteroskedastic
specifications and those with non-normal structural shocks. The
heteroskedastic SVAR model setup is similar as in Woźniak & Droumaguet
(2015) <doi:10.13140/RG.2.2.19492.55687> and Lütkepohl & Woźniak (2020)
<doi:10.1016/j.jedc.2020.103862>. The sampler of the structural matrix
follows Waggoner & Zha (2003) <doi:10.1016/S0165-1889(02)00168-9>, whereas
that for autoregressive parameters follows Chan, Koop, Yu (2022)
<https://www.joshuachan.org/papers/OISV.pdf>. The specification of Markov
switching heteroskedasticity is inspired by Song & Woźniak (2021)
<doi:10.1093/acrefore/9780190625979.013.174>, and that of Stochastic
Volatility model by Kastner & Frühwirth-Schnatter (2014)
<doi:10.1016/j.csda.2013.01.002>.

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
