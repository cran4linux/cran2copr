%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fastglmpca
%global packver   0.1-107
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.107
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Algorithms for Generalized Principal Component Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildRequires:    R-CRAN-RcppParallel >= 5.1.5
BuildRequires:    R-CRAN-Rcpp >= 1.0.8
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-distr 
BuildRequires:    R-CRAN-daarem 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-RcppParallel >= 5.1.5
Requires:         R-CRAN-Rcpp >= 1.0.8
Requires:         R-utils 
Requires:         R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-CRAN-distr 
Requires:         R-CRAN-daarem 

%description
Implements fast, scalable optimization algorithms for fitting generalized
principal components analysis (GLM-PCA) models, as described in "A
Generalization of Principal Components Analysis to the Exponential Family"
Collins M, Dasgupta S, Schapire RE (2002, ISBN:9780262271738), and
subsequently "Feature Selection and Dimension Reduction for Single-Cell
RNA-Seq Based on a Multinomial Model" Townes FW, Hicks SC, Aryee MJ,
Irizarry RA (2019) <doi:10.1186/s13059-019-1861-6>.

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
