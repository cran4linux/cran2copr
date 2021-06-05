%global packname  missSBM
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Handling Missing Data in Stochastic Block Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-nloptr >= 1.2.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sbm 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-nloptr >= 1.2.0
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sbm 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-Matrix 

%description
When a network is partially observed (here, NAs in the adjacency matrix
rather than 1 or 0 due to missing information between node pairs), it is
possible to account for the underlying process that generates those NAs.
'missSBM', presented in 'Barbillon, Chiquet and Tabouy' (2021)
<arXiv:1906.12201>, adjusts the popular stochastic block model from
network data sampled under various missing data conditions, as described
in 'Tabouy, Barbillon and Chiquet' (2019)
<doi:10.1080/01621459.2018.1562934>.

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
