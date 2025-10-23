%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NeEDS4BigData
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          New Experimental Design Based Subsampling Methods for Big Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-gam 
BuildRequires:    R-CRAN-ggh4x 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-gam 
Requires:         R-CRAN-ggh4x 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggridges 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-mvnfast 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 

%description
Subsampling methods for big data under different models and assumptions.
Starting with linear regression and leading to Generalised Linear Models,
softmax regression, and quantile regression. Specifically, the
model-robust subsampling method proposed in Mahendran, A., Thompson, H.,
and McGree, J. M. (2023) <doi:10.1007/s00362-023-01446-9>, where multiple
models can describe the big data, and the subsampling framework for
potentially misspecified Generalised Linear Models in Mahendran, A.,
Thompson, H., and McGree, J. M. (2025) <doi:10.48550/arXiv.2510.05902>.

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
