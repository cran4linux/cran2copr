%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  risdr
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Regularised and Information-Theoretic Sufficient Dimension Reduction

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 

%description
Implements covariance-stabilised sufficient dimension reduction for
continuous responses with information-theoretic structural dimension
selection. Supported methods include sliced inverse regression, sliced
average variance estimation, directional regression, and principal Hessian
directions. Sample, ridge, Oracle Approximating Shrinkage, Ledoit-Wolf,
and Maximum Entropy Covariance (MEC) estimators are provided alongside
prediction, resampling, simulation, and diagnostic utilities. The
sufficient dimension reduction methods build on Li (1991)
<doi:10.1080/01621459.1991.10475035>, Li (1992)
<doi:10.1080/01621459.1992.10476258>, and Li and Wang (2007)
<doi:10.1198/016214507000000536>. Covariance shrinkage follows Olorede and
Yahya (2019) <doi:10.48550/arXiv.1909.13017>, Ledoit and Wolf (2004)
<doi:10.1016/S0047-259X(03)00096-4> and Chen et al. (2010)
<doi:10.1109/TSP.2010.2053029>.

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
