%global packname  pcmabc
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Approximate Bayesian Computations for Phylogenetic Comparative Methods

License:          GPL (>= 2) | file LICENCE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.9.1
Requires:         R-core >= 2.9.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ape >= 3.0.6
BuildRequires:    R-CRAN-distory 
BuildRequires:    R-CRAN-geiger 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvSLOUCH 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-TreeSim 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-yuima 
Requires:         R-CRAN-ape >= 3.0.6
Requires:         R-CRAN-distory 
Requires:         R-CRAN-geiger 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-mvSLOUCH 
Requires:         R-CRAN-phangorn 
Requires:         R-stats 
Requires:         R-CRAN-TreeSim 
Requires:         R-utils 
Requires:         R-CRAN-yuima 

%description
Fits by ABC, the parameters of a stochastic process modelling the
phylogeny and evolution of a suite of traits following the tree. The user
may define an arbitrary Markov process for the trait and phylogeny.
Importantly, trait-dependent speciation models are handled and fitted to
data. See K. Bartoszek, P. Lio' (2019) <doi:10.5506/APhysPolBSupp.12.25>.

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
