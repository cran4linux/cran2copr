%global __brp_check_rpaths %{nil}
%global packname  gapclosing
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate Gaps Under an Intervention

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-stats 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-tidyselect 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 

%description
Provides functions to estimate the disparities across categories (e.g.
Black and white) that persists if a treatment variable (e.g. college) is
equalized. Makes estimates by treatment modeling, outcome modeling, and
doubly-robust augmented inverse probability weighting estimation, with
standard errors calculated by a nonparametric bootstrap. Cross-fitting is
supported. Survey weights are supported for point estimation but not for
standard error estimation; those applying this package with complex survey
samples should consult the data distributor to select an appropriate
approach for standard error construction, which may involve calling the
functions repeatedly for many sets of replicate weights provided by the
data distributor. The methods in this package are described in Lundberg
(2021) <doi:10.31235/osf.io/gx4y3>.

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
