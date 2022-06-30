%global __brp_check_rpaths %{nil}
%global packname  disclapmix
%global packver   1.7.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.4
Release:          1%{?dist}%{?buildtag}
Summary:          Discrete Laplace Mixture Inference using the EM Algorithm

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-disclap >= 1.4
BuildRequires:    R-CRAN-cluster >= 1.14.4
BuildRequires:    R-CRAN-Rcpp >= 0.11
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppProgress 
Requires:         R-CRAN-disclap >= 1.4
Requires:         R-CRAN-cluster >= 1.14.4
Requires:         R-CRAN-Rcpp >= 0.11
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-utils 

%description
Make inference in a mixture of discrete Laplace distributions using the EM
algorithm. This can e.g. be used for modelling the distribution of Y
chromosomal haplotypes as described in [1, 2] (refer to the URL section).

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
