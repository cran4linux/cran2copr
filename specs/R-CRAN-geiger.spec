%global packname  geiger
%global packver   2.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.7
Release:          2%{?dist}%{?buildtag}
Summary:          Analysis of Evolutionary Diversification

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildRequires:    R-CRAN-ape >= 3.0
BuildRequires:    R-CRAN-deSolve >= 1.7
BuildRequires:    R-CRAN-phytools >= 0.7.31
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-subplex 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-ncbit 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-methods 
Requires:         R-CRAN-ape >= 3.0
Requires:         R-CRAN-deSolve >= 1.7
Requires:         R-CRAN-phytools >= 0.7.31
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-MASS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-subplex 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-ncbit 
Requires:         R-CRAN-colorspace 
Requires:         R-methods 

%description
Methods for fitting macroevolutionary models to phylogenetic trees Pennell
(2014) <doi:10.1093/bioinformatics/btu181>.

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
