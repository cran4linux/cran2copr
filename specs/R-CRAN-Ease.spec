%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Ease
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Simulating Explicit Population Genetics Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-RcppProgress >= 0.1
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-RcppProgress >= 0.1
Requires:         R-methods 
Requires:         R-stats 

%description
Implementation in a simple and efficient way of fully customisable
population genetics simulations, considering multiple loci that have
epistatic interactions. Specifically suited to the modelling of multilocus
nucleocytoplasmic systems (with both diploid and haploid loci), it is
nevertheless possible to simulate purely diploid (or purely haploid)
genetic models. Examples of models that can be simulated with Ease are
numerous, for example models of genetic incompatibilities as presented by
Marie-Orleach et al. (2022) <doi:10.1101/2022.07.25.501356>. Many others
are conceivable, although few are actually explored, Ease having been
developed in particular to provide a solution so that these kinds of
models can be simulated simply.

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
