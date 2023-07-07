%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  secsse
%global packver   2.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Several Examined and Concealed States-Dependent Speciation and Extinction

License:          GPL (>= 3) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildRequires:    R-CRAN-DDD >= 5.0
BuildRequires:    R-CRAN-BH >= 1.81.0.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.10
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-geiger 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-DDD >= 5.0
Requires:         R-CRAN-Rcpp >= 1.0.10
Requires:         R-utils 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-geiger 
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 

%description
Simultaneously infers state-dependent diversification across two or more
states of a single or multiple traits while accounting for the role of a
possible concealed trait. See Herrera-Alsina et al. (2019)
<doi:10.1093/sysbio/syy057>.

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
