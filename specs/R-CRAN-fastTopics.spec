%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fastTopics
%global packver   0.6-186
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.186
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Algorithms for Fitting Topic Models and Non-Negative Matrix Factorizations to Count Data

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-RcppParallel >= 5.1.7
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
BuildRequires:    R-CRAN-ggrepel >= 0.9.0
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-uwot 
BuildRequires:    R-CRAN-ashr 
BuildRequires:    R-CRAN-RhpcBLASctl 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-RcppParallel >= 5.1.7
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-Rcpp >= 1.0.12
Requires:         R-CRAN-ggrepel >= 0.9.0
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-irlba 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Rtsne 
Requires:         R-CRAN-uwot 
Requires:         R-CRAN-ashr 
Requires:         R-CRAN-RhpcBLASctl 
Requires:         R-parallel 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-htmlwidgets 

%description
Implements fast, scalable optimization algorithms for fitting topic models
("grade of membership" models) and non-negative matrix factorizations to
count data. The methods exploit the special relationship between the
multinomial topic model (also, "probabilistic latent semantic indexing")
and Poisson non-negative matrix factorization. The package provides tools
to compare, annotate and visualize model fits, including functions to
efficiently create "structure plots" and identify key features in topics.
The 'fastTopics' package is a successor to the 'CountClust' package. For
more information, see <doi:10.48550/arXiv.2105.13440> and
<doi:10.1186/s13059-023-03067-9>.

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
