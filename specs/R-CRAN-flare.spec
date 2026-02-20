%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  flare
%global packver   1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Family of Lasso Regression

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-methods 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-igraph 
Requires:         R-methods 

%description
Provides implementations of a family of Lasso variants, including Dantzig
Selector, LAD Lasso, SQRT Lasso, and Lq Lasso, for estimating
high-dimensional sparse linear models. We adopt the alternating direction
method of multipliers and convert the original optimization problem into a
sequence of L1-penalized least-squares minimization problems that are
efficiently solved by linearization and multi-stage screening. In addition
to sparse linear model estimation, we provide extensions of these methods
to sparse Gaussian graphical model estimation, including TIGER and CLIME,
using either L1 or adaptive penalties. Missing values can be tolerated for
Dantzig selector and CLIME. Computation is memory-optimized using sparse
matrix output. For more information, see
<https://www.jmlr.org/papers/volume16/li15a/li15a.pdf>.

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
