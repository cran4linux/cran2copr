%global packname  babette
%global packver   2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Control 'BEAST2'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-beautier >= 2.3
BuildRequires:    R-CRAN-beastier >= 2.1.3
BuildRequires:    R-CRAN-mauricer 
BuildRequires:    R-CRAN-tracerer 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-CRAN-remotes 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-testit 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-beautier >= 2.3
Requires:         R-CRAN-beastier >= 2.1.3
Requires:         R-CRAN-mauricer 
Requires:         R-CRAN-tracerer 
Requires:         R-CRAN-phangorn 
Requires:         R-CRAN-remotes 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-testit 
Requires:         R-CRAN-xml2 

%description
'BEAST2' (<https://www.beast2.org>) is a widely used Bayesian phylogenetic
tool, that uses DNA/RNA/protein data and many model priors to create a
posterior of jointly estimated phylogenies and parameters. 'BEAST2' is
commonly accompanied by 'BEAUti 2', 'Tracer' and 'DensiTree'. 'babette'
provides for an alternative workflow of using all these tools separately.
This allows doing complex Bayesian phylogenetics easily and reproducibly
from 'R'.

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
