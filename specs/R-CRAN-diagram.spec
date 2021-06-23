%global __brp_check_rpaths %{nil}
%global packname  diagram
%global packver   1.6.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.5
Release:          1%{?dist}%{?buildtag}
Summary:          Functions for Visualising Simple Graphs (Networks), Plotting Flow Diagrams

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.01
Requires:         R-core >= 2.01
BuildArch:        noarch
BuildRequires:    R-CRAN-shape 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-shape 
Requires:         R-stats 
Requires:         R-graphics 

%description
Visualises simple graphs (networks) based on a transition matrix,
utilities to plot flow diagrams, visualising webs, electrical networks,
etc. Support for the book "A practical guide to ecological modelling -
using R as a simulation platform" by Karline Soetaert and Peter M.J.
Herman (2009), Springer. and the book "Solving Differential Equations in
R" by Karline Soetaert, Jeff Cash and Francesca Mazzia (2012), Springer.
Includes demo(flowchart), demo(plotmat), demo(plotweb).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
