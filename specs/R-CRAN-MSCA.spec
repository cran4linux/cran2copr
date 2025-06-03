%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MSCA
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Unsupervised Clustering of Multiple Censored Time-to-Event Endpoints

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-RcppParallel >= 5.1.10
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-fastkmedoids 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-RcppParallel >= 5.1.10
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-fastkmedoids 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Matrix 

%description
Provides basic tools and wrapper functions for computing clusters of
instances described by multiple time-to-event censored endpoints. From
long-format datasets, where one instance is described by one or more dated
records, the main function, `make_state_matrices()`, creates state
matrices. Based on these matrices, optimised procedures using the Jaccard
distance between instances enable the construction of longitudinal
typologies. The package is under active development, with additional tools
for graphical representation of typologies planned. For methodological
details, see our accompanying paper: `Delord M, Douiri A (2025)
<doi:10.1186/s12874-025-02476-7>`.

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
