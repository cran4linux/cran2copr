%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  baggingbwsel
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bagging Bandwidth Selection in Kernel Density and Regression Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-kedd 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sm 
BuildRequires:    R-CRAN-nor1mix 
BuildRequires:    R-CRAN-misc3d 
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-kedd 
Requires:         R-stats 
Requires:         R-CRAN-sm 
Requires:         R-CRAN-nor1mix 
Requires:         R-CRAN-misc3d 

%description
Bagging bandwidth selection methods for the Parzen-Rosenblatt and
Nadaraya-Watson estimators. These bandwidth selectors can achieve greater
statistical precision than their non-bagged counterparts while being
computationally fast. See Barreiro-Ures et al. (2020)
<doi:10.1093/biomet/asaa092> and Barreiro-Ures et al. (2021)
<doi:10.48550/arXiv.2105.04134>.

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
