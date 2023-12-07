%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CovRegRF
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Covariance Regression with Random Forests

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-data.tree 
BuildRequires:    R-CRAN-DiagrammeR 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-data.tree 
Requires:         R-CRAN-DiagrammeR 

%description
Covariance Regression with Random Forests ('CovRegRF') is a random forest
method for estimating the covariance matrix of a multivariate response
given a set of covariates. Random forest trees are built with a new
splitting rule which is designed to maximize the distance between the
sample covariance matrix estimates of the child nodes. The method is
described in Alakus et al. (2023) <doi:10.1186/s12859-023-05377-y>.
'CovRegRF' uses 'randomForestSRC' package (Ishwaran and Kogalur, 2022)
<https://cran.r-project.org/package=randomForestSRC> by freezing at the
version 3.1.0. The custom splitting rule feature is utilised to apply the
proposed splitting rule. 'LAPACK' and 'BLAS' libraries are used for matrix
decompositions. The 'CovRegRF' package includes the header files
'lapacke.h' and 'cblas.h' from the 'LAPACK' and 'BLAS' libraries. The
'LAPACK' library is licensed under modified BSD license.

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
