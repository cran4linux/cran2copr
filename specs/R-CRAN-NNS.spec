%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NNS
%global packver   11.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          11.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Nonlinear Nonparametric Statistics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-quantmod 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-quantmod 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 

%description
NNS (Nonlinear Nonparametric Statistics) leverages partial moments – the
fundamental elements of variance that asymptotically approximate the area
under f(x) – to provide a robust foundation for nonlinear analysis while
maintaining linear equivalences.  NNS delivers a comprehensive suite of
advanced statistical techniques, including: Numerical integration,
Numerical differentiation, Clustering, Correlation, Dependence, Causal
analysis, ANOVA, Regression, Classification, Seasonality, Autoregressive
modeling, Normalization, Stochastic dominance and Advanced Monte Carlo
sampling.  All routines based on: Viole, F. and Nawrocki, D. (2013),
Nonlinear Nonparametric Statistics: Using Partial Moments (ISBN:
1490523995).

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
