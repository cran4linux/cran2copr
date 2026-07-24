%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  coalescentMCMC
%global packver   0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5
Release:          1%{?dist}%{?buildtag}
Summary:          MCMC Algorithms for the Coalescent

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-splines 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-phangorn 
Requires:         R-splines 
Requires:         R-stats 
Requires:         R-utils 

%description
Flexible framework for coalescent analyses in R. It includes a main
function running the MCMC algorithm, auxiliary functions for tree
rearrangement, and some functions to compute population genetic
parameters. Extended description can be found in Paradis (2020)
<doi:10.1201/9780429466700>. For details on the MCMC algorithm, see Kuhner
et al. (1995) <doi:10.1093/genetics/140.4.1421> and Drummond et al. (2002)
<doi:10.1093/genetics/161.3.1307>.

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
