%global packname  mcbette
%global packver   1.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.13
Release:          1%{?dist}%{?buildtag}
Summary:          Model Comparison Using 'babette'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-beautier >= 2.4
BuildRequires:    R-CRAN-mauricer >= 2.3
BuildRequires:    R-CRAN-beastier >= 2.2.1
BuildRequires:    R-CRAN-babette >= 2.1
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-Rmpfr 
BuildRequires:    R-CRAN-testit 
BuildRequires:    R-CRAN-txtplot 
Requires:         R-CRAN-beautier >= 2.4
Requires:         R-CRAN-mauricer >= 2.3
Requires:         R-CRAN-beastier >= 2.2.1
Requires:         R-CRAN-babette >= 2.1
Requires:         R-CRAN-curl 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-Rmpfr 
Requires:         R-CRAN-testit 
Requires:         R-CRAN-txtplot 

%description
'BEAST2' (<https://www.beast2.org>) is a widely used Bayesian phylogenetic
tool, that uses DNA/RNA/protein data and many model priors to create a
posterior of jointly estimated phylogenies and parameters. 'mcbette'
allows to do a Bayesian model comparison over some site and clock models,
using 'babette' (<https://github.com/ropensci/babette/>).

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
