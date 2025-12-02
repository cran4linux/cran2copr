%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DSFM
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Distributed Skew Factor Model Estimation Methods

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-elasticnet 
BuildRequires:    R-CRAN-SOPC 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-sn 
Requires:         R-stats 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-elasticnet 
Requires:         R-CRAN-SOPC 

%description
Provides a distributed framework for simulating and estimating skew factor
models under various skewed and heavy-tailed distributions. The methods
support distributed data generation, aggregation of local estimators, and
evaluation of estimation performance via mean squared error, relative
error, and sparsity measures. The distributed principal component (PC)
estimators implemented in the package include 'IPC' (Independent Principal
Component),'PPC' (Project Principal Component), 'SPC' (Sparse Principal
Component), and other related distributed PC methods. The methodological
background follows Guo G. (2023) <doi:10.1007/s00180-022-01270-z>.

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
