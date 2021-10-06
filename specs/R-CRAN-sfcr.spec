%global __brp_check_rpaths %{nil}
%global packname  sfcr
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simulate Stock-Flow Consistent Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-tibble >= 3.0.3
BuildRequires:    R-CRAN-Rdpack >= 2.1
BuildRequires:    R-CRAN-rootSolve >= 1.8.2.1
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-kableExtra >= 1.3.1
BuildRequires:    R-CRAN-igraph >= 1.2.6
BuildRequires:    R-CRAN-tidyr >= 1.1.2
BuildRequires:    R-CRAN-tidyselect >= 1.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
BuildRequires:    R-CRAN-dplyr >= 1.0.2
BuildRequires:    R-CRAN-expm >= 0.999.5
BuildRequires:    R-CRAN-forcats >= 0.5.0
BuildRequires:    R-CRAN-rlang >= 0.4.7
BuildRequires:    R-CRAN-vctrs >= 0.3.5
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-tibble >= 3.0.3
Requires:         R-CRAN-Rdpack >= 2.1
Requires:         R-CRAN-rootSolve >= 1.8.2.1
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-kableExtra >= 1.3.1
Requires:         R-CRAN-igraph >= 1.2.6
Requires:         R-CRAN-tidyr >= 1.1.2
Requires:         R-CRAN-tidyselect >= 1.1.0
Requires:         R-CRAN-Rcpp >= 1.0.5
Requires:         R-CRAN-dplyr >= 1.0.2
Requires:         R-CRAN-expm >= 0.999.5
Requires:         R-CRAN-forcats >= 0.5.0
Requires:         R-CRAN-rlang >= 0.4.7
Requires:         R-CRAN-vctrs >= 0.3.5
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-utils 

%description
Routines to write, simulate, and validate stock-flow consistent (SFC)
models. The accounting structure of SFC models are described in Godley and
Lavoie (2007, ISBN:978-1-137-08599-3). The algorithms implemented to solve
the models (Gauss-Seidel and Broyden) are described in Kinsella and O'Shea
(2010) <doi:10.2139/ssrn.1729205> and Peressini and Sullivan (1988,
ISBN:0-387-96614-5).

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
