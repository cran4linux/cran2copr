%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ashr
%global packver   2.2-63
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.63
Release:          1%{?dist}%{?buildtag}
Summary:          Methods for Adaptive Shrinkage, using Empirical Bayes

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Rcpp >= 0.10.5
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-mixsqp 
BuildRequires:    R-CRAN-SQUAREM 
BuildRequires:    R-CRAN-etrunct 
BuildRequires:    R-CRAN-invgamma 
Requires:         R-CRAN-Rcpp >= 0.10.5
Requires:         R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-mixsqp 
Requires:         R-CRAN-SQUAREM 
Requires:         R-CRAN-etrunct 
Requires:         R-CRAN-invgamma 

%description
The R package 'ashr' implements an Empirical Bayes approach for
large-scale hypothesis testing and false discovery rate (FDR) estimation
based on the methods proposed in M. Stephens, 2016, "False discovery
rates: a new deal", <DOI:10.1093/biostatistics/kxw041>. These methods can
be applied whenever two sets of summary statistics---estimated effects and
standard errors---are available, just as 'qvalue' can be applied to
previously computed p-values. Two main interfaces are provided: ash(),
which is more user-friendly; and ash.workhorse(), which has more options
and is geared toward advanced users. The ash() and ash.workhorse() also
provides a flexible modeling interface that can accommodate a variety of
likelihoods (e.g., normal, Poisson) and mixture priors (e.g., uniform,
normal).

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
