%global __brp_check_rpaths %{nil}
%global packname  beastier
%global packver   2.4.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.9
Release:          1%{?dist}%{?buildtag}
Summary:          Call 'BEAST2'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-beautier >= 2.6.1
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-assertive 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-beautier >= 2.6.1
Requires:         R-CRAN-ape 
Requires:         R-CRAN-assertive 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-phangorn 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rJava 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-xml2 

%description
'BEAST2' (<https://www.beast2.org>) is a widely used Bayesian phylogenetic
tool, that uses DNA/RNA/protein data and many model priors to create a
posterior of jointly estimated phylogenies and parameters. 'BEAST2' is a
command-line tool. This package provides a way to call 'BEAST2' from an
'R' function call.

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
