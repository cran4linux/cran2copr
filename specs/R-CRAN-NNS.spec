%global __brp_check_rpaths %{nil}
%global packname  NNS
%global packver   0.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          1%{?dist}%{?buildtag}
Summary:          Nonlinear Nonparametric Statistics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dtw 
BuildRequires:    R-CRAN-dynlm 
BuildRequires:    R-CRAN-meboot 
BuildRequires:    R-CRAN-Quandl 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tdigest 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dtw 
Requires:         R-CRAN-dynlm 
Requires:         R-CRAN-meboot 
Requires:         R-CRAN-Quandl 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tdigest 
Requires:         R-CRAN-zoo 

%description
Nonlinear nonparametric statistics using partial moments.  Partial moments
are the elements of variance and asymptotically approximate the area of
f(x).  These robust statistics provide the basis for nonlinear analysis
while retaining linear equivalences.  NNS offers: Numerical integration,
Numerical differentiation, Clustering, Correlation, Dependence, Causal
analysis, ANOVA, Regression, Classification, Seasonality, Autoregressive
modeling, Normalization and Stochastic dominance.  All routines based on:
Viole, F. and Nawrocki, D. (2013), Nonlinear Nonparametric Statistics:
Using Partial Moments (ISBN: 1490523995).

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
