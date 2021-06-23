%global __brp_check_rpaths %{nil}
%global packname  PantaRhei
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Plots Sankey Diagrams

License:          EUPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-grid 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-grid 
Requires:         R-grDevices 
Requires:         R-utils 

%description
Sankey diagrams are a powerfull and visually attractive way to visualize
the flow of conservative substances through a system. They typically
consists of a network of nodes, and fluxes between them, where the total
balance in each internal node is 0, i.e. input equals output. Sankey
diagrams are typically used to display energy systems, material flow
accounts etc. Unlike so-called alluvial plots, Sankey diagrams also allow
for cyclic flows: flows originating from a single node can, either direct
or indirect, contribute to the input of that same node. This package,
named after the Greek aphorism Panta Rhei (everything flows), provides
functions to create publication-quality diagrams, using data in tables (or
spread sheets) and a simple syntax.

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
