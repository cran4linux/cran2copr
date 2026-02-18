%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  exametrika
%global packver   1.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.1
Release:          1%{?dist}%{?buildtag}
Summary:          Test Theory Analysis and Biclustering

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-igraph 

%description
Implements comprehensive test data engineering methods as described in
Shojima (2022, ISBN:978-9811699856). Provides statistical techniques for
engineering and processing test data: Classical Test Theory (CTT) with
reliability coefficients for continuous ability assessment; Item Response
Theory (IRT) including Rasch, 2PL, and 3PL models with item/test
information functions; Latent Class Analysis (LCA) for nominal clustering;
Latent Rank Analysis (LRA) for ordinal clustering with automatic
determination of cluster numbers; Biclustering methods including infinite
relational models for simultaneous clustering of examinees and items
without predefined cluster numbers; and Bayesian Network Models (BNM) for
visualizing inter-item dependencies. Features local dependence analysis
through LRA and biclustering, parameter estimation, dimensionality
assessment, and network structure visualization for educational,
psychological, and social science research.

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
