%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  xLLiM
%global packver   2.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          High Dimensional Locally-Linear Mapping

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-capushe 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-mda 
BuildRequires:    R-CRAN-progress 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-capushe 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-mda 
Requires:         R-CRAN-progress 

%description
Provides a tool for non linear mapping (non linear regression) using a
mixture of regression model and an inverse regression strategy. The
methods include the GLLiM model (see Deleforge et al (2015)
<DOI:10.1007/s11222-014-9461-5>) based on Gaussian mixtures and a robust
version of GLLiM, named SLLiM (see Perthame et al (2016)
<DOI:10.1016/j.jmva.2017.09.009>) based on a mixture of Generalized
Student distributions. The methods also include BLLiM (see Devijver et al
(2017) <arXiv:1701.07899>) which is an extension of GLLiM with a sparse
block diagonal structure for large covariance matrices (particularly
interesting for transcriptomic data).

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
