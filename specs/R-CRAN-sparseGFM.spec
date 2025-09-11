%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sparseGFM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Sparse Generalized Factor Models with Multiple Penalty Functions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-GFM 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-irlba 
Requires:         R-stats 
Requires:         R-CRAN-GFM 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-irlba 

%description
Implements sparse generalized factor models (sparseGFM) for dimension
reduction and variable selection in high-dimensional data with automatic
adaptation to weak factor scenarios. The package supports multiple data
types (continuous, count, binary) through generalized linear model
frameworks and handles missing values automatically. It provides 12
different penalty functions including Least Absolute Shrinkage and
Selection Operator (Lasso), adaptive Lasso, Smoothly Clipped Absolute
Deviation (SCAD), Minimax Concave Penalty (MCP), group Lasso, and their
adaptive versions for inducing row-wise sparsity in factor loadings. Key
features include cross-validation for regularization parameter selection
using Sparsity Information Criterion (SIC), automatic determination of the
number of factors via multiple information criteria, and specialized
algorithms for row-sparse loading structures. The methodology employs
alternating minimization with Singular Value Decomposition (SVD)-based
identifiability constraints and is particularly effective for
high-dimensional applications in genomics, economics, and social sciences
where interpretable sparse dimension reduction is crucial. For penalty
functions, see Tibshirani (1996) <doi:10.1111/j.2517-6161.1996.tb02080.x>,
Fan and Li (2001) <doi:10.1198/016214501753382273>, and Zhang (2010)
<doi:10.1214/09-AOS729>.

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
