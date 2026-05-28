%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CoalescentPhylo
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Phylogenetics via Root Distances Method Under the Coalescent

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-CRAN-rootSolve 
Requires:         R-CRAN-ape 
Requires:         R-parallel 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-phangorn 
Requires:         R-CRAN-rootSolve 

%description
Estimates phylogenetic trees from allele count data using the root
distance method under the Coalescent Model. Given a matrix of allele
counts across taxa and loci, the package estimates pairwise root distances
under the Coalescent Model using maximum likelihood estimation. Then, it
estimates a labeled phylogenetic tree from the estimated root distances.
See Peng et al. (2021) <doi:10.1016/j.ympev.2021.107142>.

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
