%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  quantreg
%global packver   5.98
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.98
Release:          1%{?dist}%{?buildtag}
Summary:          Quantile Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-SparseM 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-MatrixModels 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-SparseM 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-MatrixModels 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-MASS 

%description
Estimation and inference methods for models for conditional quantile
functions: Linear and nonlinear parametric and non-parametric (total
variation penalized) models for conditional quantiles of a univariate
response and several methods for handling censored survival data.
Portfolio selection methods based on expected shortfall risk are also now
included. See Koenker, R. (2005) Quantile Regression, Cambridge U. Press,
<doi:10.1017/CBO9780511754098> and Koenker, R. et al. (2017) Handbook of
Quantile Regression, CRC Press, <doi:10.1201/9781315120256>.

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
