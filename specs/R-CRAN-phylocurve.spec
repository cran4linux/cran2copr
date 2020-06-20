%global packname  phylocurve
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}
Summary:          Phylogenetic Comparative Methods for High-Dimensional Traits

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-geomorph >= 3.0.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-drc 
BuildRequires:    R-CRAN-dtw 
BuildRequires:    R-CRAN-geiger 
BuildRequires:    R-CRAN-GPfit 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-phylolm 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-geomorph >= 3.0.0
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-drc 
Requires:         R-CRAN-dtw 
Requires:         R-CRAN-geiger 
Requires:         R-CRAN-GPfit 
Requires:         R-Matrix 
Requires:         R-CRAN-phylolm 
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Tools for studying the evolution of high-dimensional traits (morphometric,
function-valued, etc.) including ancestral state reconstruction,
estimating phylogenetic signal, and assessing correlated trait evolution.
Visit <http://www.phylocurve.org> for more information.

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

%files
%{rlibdir}/%{packname}
