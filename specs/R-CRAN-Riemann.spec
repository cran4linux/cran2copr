%global packname  Riemann
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Learning with Data on Riemannian Manifolds

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
BuildRequires:    R-CRAN-CVXR 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-RiemBase 
BuildRequires:    R-CRAN-Rdimtools 
BuildRequires:    R-CRAN-T4cluster 
BuildRequires:    R-CRAN-DEoptim 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-maotai 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.5
Requires:         R-CRAN-CVXR 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-RiemBase 
Requires:         R-CRAN-Rdimtools 
Requires:         R-CRAN-T4cluster 
Requires:         R-CRAN-DEoptim 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-maotai 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-ggrepel 

%description
We provide a variety of algorithms for manifold-valued data, including
Fréchet summaries, hypothesis testing, clustering, visualization, and
other learning tasks. See Bhattacharya and Bhattacharya (2012)
<doi:10.1017/CBO9781139094764> for general exposition to statistics on
manifolds.

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
