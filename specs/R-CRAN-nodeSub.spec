%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nodeSub
%global packver   1.2.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.9
Release:          1%{?dist}%{?buildtag}
Summary:          Simulate DNA Alignments Using Node Substitutions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-beastier 
BuildRequires:    R-CRAN-beautier 
BuildRequires:    R-CRAN-DDD 
BuildRequires:    R-CRAN-geiger 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-CRAN-phylobase 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-Rmpfr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-testit 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tracerer 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-beastier 
Requires:         R-CRAN-beautier 
Requires:         R-CRAN-DDD 
Requires:         R-CRAN-geiger 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-phangorn 
Requires:         R-CRAN-phylobase 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-Rmpfr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-testit 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tracerer 

%description
Simulate DNA sequences for the node substitution model.  In the node
substitution model, substitutions accumulate additionally during a
speciation event, providing a potential mechanistic explanation for
substitution rate variation. This package provides tools to simulate such
a process, simulate a reference process with only substitutions along the
branches, and provides tools to infer phylogenies from alignments. More
information can be found in Janzen (2021) <doi:10.1093/sysbio/syab085>.

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
