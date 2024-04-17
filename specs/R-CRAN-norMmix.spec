%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  norMmix
%global packver   0.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Direct MLE for Multivariate Normal Mixture Distributions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-sfsmisc 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-sfsmisc 

%description
Multivariate Normal (i.e. Gaussian) Mixture Models (S3) Classes. Fitting
models to data using MLE (maximum likelihood estimation) for multivariate
normal mixtures via smart parametrization using the LDLt (Cholesky)
decomposition. McLachlan, G. and Peel, D. (2000, ISBN:9780471006268)
"Finite Mixture Models". Celeux, G. and Govaert, G. (1995)
<doi:10.1016/0031-3203(94)00125-6> "Gaussian parsimonious clustering
models". Marron, S. and Wand, M. (1992) <doi:10.1214/aos/1176348653>
"Exact Mean Integrated Squared Error".

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
