%global __brp_check_rpaths %{nil}
%global packname  flare
%global packver   1.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.0
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
Provide the implementation of a family of Lasso variants including Dantzig
Selector, LAD Lasso, SQRT Lasso, Lq Lasso for estimating high dimensional
sparse linear model. We adopt the alternating direction method of
multipliers and convert the original optimization problem into a
sequential L1 penalized least square minimization problem, which can be
efficiently solved by linearization algorithm. A multi-stage screening
approach is adopted for further acceleration. Besides the sparse linear
model estimation, we also provide the extension of these Lasso variants to
sparse Gaussian graphical model estimation including TIGER and CLIME using
either L1 or adaptive penalty. Missing values can be tolerated for Dantzig
selector and CLIME. The computation is memory-optimized using the sparse
matrix output. For more information, please refer to
<https://www.jmlr.org/papers/volume16/li15a/li15a.pdf>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
