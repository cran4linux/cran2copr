%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pedbuildr
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Pedigree Reconstruction

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pedtools >= 2.2.0
BuildRequires:    R-CRAN-forrel >= 1.5.0
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-pedmut 
BuildRequires:    R-CRAN-pedprobr 
BuildRequires:    R-CRAN-ribd 
Requires:         R-CRAN-pedtools >= 2.2.0
Requires:         R-CRAN-forrel >= 1.5.0
Requires:         R-CRAN-glue 
Requires:         R-CRAN-pedmut 
Requires:         R-CRAN-pedprobr 
Requires:         R-CRAN-ribd 

%description
Reconstruct pedigrees from genotype data, by optimising the likelihood
over all possible pedigrees subject to given restrictions. Tailor-made
plots facilitate evaluation of the output. This package is part of the
'pedsuite' ecosystem for pedigree analysis. In particular, it imports
'pedprobr' for calculating pedigree likelihoods and 'forrel' for
estimating pairwise relatedness.

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
