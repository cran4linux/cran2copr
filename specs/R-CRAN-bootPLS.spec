%global __brp_check_rpaths %{nil}
%global packname  bootPLS
%global packver   0.9.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.9
Release:          1%{?dist}%{?buildtag}
Summary:          Bootstrap Hyperparameter Selection for PLS Models and Extensions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-plsRglm 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-spls 
BuildRequires:    R-CRAN-bipartite 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-plsRglm 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-spls 
Requires:         R-CRAN-bipartite 
Requires:         R-CRAN-mvtnorm 

%description
Several implementations of non-parametric stable bootstrap-based
techniques to determine the numbers of components for Partial Least
Squares linear or generalized linear regression models as well as and
sparse Partial Least Squares linear or generalized linear regression
models. The package collects techniques that were published in a book
chapter (Magnanensi et al. 2016, 'The Multiple Facets of Partial Least
Squares and Related Methods', <doi:10.1007/978-3-319-40643-5_18>) and two
articles (Magnanensi et al. 2017, 'Statistics and Computing',
<doi:10.1007/s11222-016-9651-4>) and (Magnanensi et al. 2021, 'Frontiers
in Applied Mathematics and Statistics', accepted.).

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
