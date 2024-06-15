%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  crossurr
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Cross-Fitting for Doubly Robust Evaluation of High-Dimensional Surrogate Markers

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-RCAL 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-SIS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-SuperLearner 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-glue 
Requires:         R-parallel 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-RCAL 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-SIS 
Requires:         R-stats 
Requires:         R-CRAN-SuperLearner 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
Doubly robust methods for evaluating surrogate markers as outlined in:
Agniel D, Hejblum BP, Thiebaut R & Parast L (2022). "Doubly robust
evaluation of high-dimensional surrogate markers", Biostatistics
<doi:10.1093/biostatistics/kxac020>. You can use these methods to
determine how much of the overall treatment effect is explained by a
(possibly high-dimensional) set of surrogate markers.

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
