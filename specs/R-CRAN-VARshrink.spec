%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  VARshrink
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Shrinkage Estimation Methods for Vector Autoregressive Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-corpcor >= 1.6.9
BuildRequires:    R-CRAN-vars >= 1.6.1
BuildRequires:    R-CRAN-ars >= 0.6
BuildRequires:    R-CRAN-strucchange 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-corpcor >= 1.6.9
Requires:         R-CRAN-vars >= 1.6.1
Requires:         R-CRAN-ars >= 0.6
Requires:         R-CRAN-strucchange 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mvtnorm 

%description
Vector autoregressive (VAR) model is a fundamental and effective approach
for multivariate time series analysis. Shrinkage estimation methods can be
applied to high-dimensional VAR models with dimensionality greater than
the number of observations, contrary to the standard ordinary least
squares method. This package is an integrative package delivering
nonparametric, parametric, and semiparametric methods in a unified and
consistent manner, such as the multivariate ridge regression in Golub,
Heath, and Wahba (1979) <doi:10.2307/1268518>, a James-Stein type
nonparametric shrinkage method in Opgen-Rhein and Strimmer (2007)
<doi:10.1186/1471-2105-8-S2-S3>, and Bayesian estimation methods using
noninformative and informative priors in Lee, Choi, and S.-H. Kim (2016)
<doi:10.1016/j.csda.2016.03.007> and Ni and Sun (2005)
<doi:10.1198/073500104000000622>.

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
