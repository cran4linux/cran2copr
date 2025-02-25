%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MSTest
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Hypothesis Testing for Markov Switching Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-GenSA 
BuildRequires:    R-CRAN-pso 
BuildRequires:    R-CRAN-GA 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-stats 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-GenSA 
Requires:         R-CRAN-pso 
Requires:         R-CRAN-GA 
Requires:         R-graphics 

%description
Implementation of hypothesis testing procedures described in Hansen (1992)
<doi:10.1002/jae.3950070506>, Carrasco, Hu, & Ploberger (2014)
<doi:10.3982/ECTA8609>, Dufour & Luger (2017)
<doi:10.1080/07474938.2017.1307548>, and Rodriguez Rondon & Dufour (2024)
<https://grodriguezrondon.com/files/RodriguezRondon_Dufour_2024_MonteCarlo_LikelihoodRatioTest_MarkovSwitchingModels_20241015.pdf>
that can be used to identify the number of regimes in Markov switching
models.

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
