%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  beautier
%global packver   2.6.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.6.5
Release:          1%{?dist}%{?buildtag}
Summary:          'BEAUti' from R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-assertive 
BuildRequires:    R-CRAN-pryr 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-seqinr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-testit 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-assertive 
Requires:         R-CRAN-pryr 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-seqinr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-testit 

%description
'BEAST2' (<https://www.beast2.org>) is a widely used Bayesian phylogenetic
tool, that uses DNA/RNA/protein data and many model priors to create a
posterior of jointly estimated phylogenies and parameters. 'BEAUti 2'
(which is part of 'BEAST2') is a GUI tool that allows users to specify the
many possible setups and generates the XML file 'BEAST2' needs to run.
This package provides a way to create 'BEAST2' input files without active
user input, but using R function calls instead.

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
