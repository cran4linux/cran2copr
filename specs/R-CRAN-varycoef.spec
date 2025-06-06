%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  varycoef
%global packver   0.3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.6
Release:          1%{?dist}%{?buildtag}
Summary:          Modeling Spatially Varying Coefficients

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-optimParallel >= 0.8.1
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mlr 
BuildRequires:    R-CRAN-mlrMBO 
BuildRequires:    R-CRAN-ParamHelpers 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-smoof 
BuildRequires:    R-CRAN-spam 
Requires:         R-CRAN-optimParallel >= 0.8.1
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-lhs 
Requires:         R-methods 
Requires:         R-CRAN-mlr 
Requires:         R-CRAN-mlrMBO 
Requires:         R-CRAN-ParamHelpers 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-smoof 
Requires:         R-CRAN-spam 

%description
Implements a maximum likelihood estimation (MLE) method for estimation and
prediction of Gaussian process-based spatially varying coefficient (SVC)
models (Dambon et al. (2021a) <doi:10.1016/j.spasta.2020.100470>).
Covariance tapering (Furrer et al. (2006) <doi:10.1198/106186006X132178>)
can be applied such that the method scales to large data. Further, it
implements a joint variable selection of the fixed and random effects
(Dambon et al. (2021b) <doi:10.1080/13658816.2022.2097684>). The package
and its capabilities are described in (Dambon et al. (2021c)
<doi:10.48550/arXiv.2106.02364>).

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
