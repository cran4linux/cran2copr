%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gadget3
%global packver   0.13-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.13.0
Release:          1%{?dist}%{?buildtag}
Summary:          Globally-Applicable Area Disaggregated General Ecosystem Toolbox V3

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-TMB >= 1.7.0
BuildRequires:    R-CRAN-rlang >= 0.4.5
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-TMB >= 1.7.0
Requires:         R-CRAN-rlang >= 0.4.5
Requires:         R-CRAN-digest 
Requires:         R-stats 
Requires:         R-utils 

%description
A framework to assist creation of marine ecosystem models, generating
either 'R' or 'C++' code which can then be optimised using the 'TMB'
package and standard 'R' tools. Principally designed to reproduce gadget2
models in 'TMB', but can be extended beyond gadget2's capabilities. Kasper
Kristensen, Anders Nielsen, Casper W. Berg, Hans Skaug, Bradley M. Bell
(2016) <doi:10.18637/jss.v070.i05> "TMB: Automatic Differentiation and
Laplace Approximation.". Begley, J., & Howell, D. (2004)
<https://core.ac.uk/download/pdf/225936648.pdf> "An overview of Gadget,
the globally applicable area-disaggregated general ecosystem toolbox.
ICES.".

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
