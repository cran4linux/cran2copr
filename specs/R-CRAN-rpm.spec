%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rpm
%global packver   0.7-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.4
Release:          1%{?dist}%{?buildtag}
Summary:          Modeling of Revealed Preferences Matchings

License:          GPL-3 + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-doFuture 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-future 
Requires:         R-CRAN-doRNG 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-doFuture 
Requires:         R-CRAN-foreach 

%description
Statistical estimation of revealed preference models from data collected
on bipartite matchings. The models are for matchings within a bipartite
population where individuals have utility for people based on known and
unknown characteristics. People can form a partnership or remain
unpartnered. The model represents both the availability of potential
partners of different types and preferences of individuals for such
people. The software estimates preference parameters based on sample
survey data on partnerships and population composition. The simulation of
matchings and goodness-of-fit are considered.  See Goyal, Handcock,
Jackson, Rendall and Yeung (2022) <doi:10.1093/jrsssa/qnad031>.

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
