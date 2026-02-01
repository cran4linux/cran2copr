%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GPvecchia
%global packver   0.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Scalable Gaussian-Process Approximations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Matrix >= 1.5.1
BuildRequires:    R-CRAN-Rcpp >= 1.1.1
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sparseinv 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-GpGp 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Matrix >= 1.5.1
Requires:         R-CRAN-Rcpp >= 1.1.1
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-sparseinv 
Requires:         R-CRAN-fields 
Requires:         R-parallel 
Requires:         R-CRAN-GpGp 
Requires:         R-CRAN-FNN 

%description
Fast scalable Gaussian process approximations, particularly well suited to
spatial (aerial, remote-sensed) and environmental data, described in more
detail in Katzfuss and Guinness (2017) <doi:10.48550/arXiv.1708.06302>.
Package also contains a fast implementation of the incomplete Cholesky
decomposition (IC0), based on Schaefer et al. (2019)
<doi:10.48550/arXiv.1706.02205> and MaxMin ordering proposed in Guinness
(2018) <doi:10.48550/arXiv.1609.05372>.

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
