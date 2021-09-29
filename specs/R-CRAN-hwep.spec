%global __brp_check_rpaths %{nil}
%global packname  hwep
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Hardy-Weinberg Equilibrium in Polyploids

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-doFuture 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-tensr 
BuildRequires:    R-CRAN-doRNG 
Requires:         R-CRAN-future 
Requires:         R-CRAN-doFuture 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-tensr 
Requires:         R-CRAN-doRNG 

%description
Inference concerning equilibrium and random mating in autopolyploids.
Methods are available to test for equilibrium and random mating at any
even ploidy level (>2) in the presence of double reduction at biallelic
loci. For autopolyploid populations in equilibrium, methods are available
to estimate the degree of double reduction. We also provide functions to
calculate genotype frequencies at equilibrium, or after one or several
rounds of random mating, given rates of double reduction. The main
function is `hwefit()`. This material is based upon work supported by the
National Science Foundation under Grant No. 2132247. The opinions,
findings, and conclusions or recommendations expressed are those of the
author and do not necessarily reflect the views of the National Science
Foundation. For details of these methods, see Gerard (2021)
<doi:10.1101/2021.09.24.461731>.

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
