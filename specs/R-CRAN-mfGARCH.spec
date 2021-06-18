%global packname  mfGARCH
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Mixed-Frequency GARCH Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-maxLik 
Requires:         R-CRAN-Rcpp 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-maxLik 

%description
Estimating GARCH-MIDAS (MIxed-DAta-Sampling) models (Engle, Ghysels, Sohn,
2013, <doi:10.1162/REST_a_00300>) and related statistical inference,
accompanying the paper "Two are better than one: Volatility forecasting
using multiplicative component GARCH models" by Conrad and Kleen (2020,
<doi:10.1002/jae.2742>). The GARCH-MIDAS model decomposes the conditional
variance of (daily) stock returns into a short- and long-term component,
where the latter may depend on an exogenous covariate sampled at a lower
frequency.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
