%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  auxvecLASSO
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          LASSO Auxiliary Variable Selection and Auxiliary Vector Diagnostics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5.0
Requires:         R-core >= 4.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-parallelly 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-crayon 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-parallelly 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-glmnet 
Requires:         R-stats 
Requires:         R-CRAN-survey 
Requires:         R-utils 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-crayon 

%description
Provides tools for assessing and selecting auxiliary variables using
LASSO. The package includes functions for variable selection and
diagnostics, facilitating survey calibration analysis with emphasis on
robust auxiliary vector selection. For more details see Tibshirani (1996)
<doi:10.1111/j.2517-6161.1996.tb02080.x> and Caughrey and Hartman (2017)
<doi:10.2139/ssrn.3494436>.

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
