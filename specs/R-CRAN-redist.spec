%global packname  redist
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Simulation Methods for Legislative Redistricting

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gmp-devel
BuildRequires:    libxml2-devel
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-lwgeom 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-servr 
BuildRequires:    R-CRAN-sys 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-coda 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-lwgeom 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-servr 
Requires:         R-CRAN-sys 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-stringr 

%description
Enables researchers to sample redistricting plans from a pre-specified
target distribution using Sequential Monte Carlo and Markov Chain Monte
Carlo algorithms.  The package allows for the implementation of various
constraints in the redistricting process such as geographic compactness
and population parity requirements. Tools for analysis such as computation
of various summary statistics and plotting functionality are also
included. The package implements methods described in Fifield, Higgins,
Imai and Tarr (2020) <doi: 10.1080/10618600.2020.1739532>, Fifield, Imai,
Kawahara, and Kenny (2020) <doi: 10.1080/2330443X.2020.1791773>, and
McCartan and Imai (2020) <arXiv: 2008.06131>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
