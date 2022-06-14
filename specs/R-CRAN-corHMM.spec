%global __brp_check_rpaths %{nil}
%global packname  corHMM
%global packver   2.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.8
Release:          1%{?dist}%{?buildtag}
Summary:          Hidden Markov Models of Character Evolution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-GenSA 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-Rmpfr 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-phytools 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-GenSA 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-phangorn 
Requires:         R-parallel 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-Rmpfr 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-phytools 

%description
Fits hidden Markov models of discrete character evolution which allow
different transition rate classes on different portions of a phylogeny.
Beaulieu et al (2013) <doi:10.1093/sysbio/syt034>.

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
