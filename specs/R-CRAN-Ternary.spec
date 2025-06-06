%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Ternary
%global packver   2.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.4
Release:          1%{?dist}%{?buildtag}
Summary:          Create Ternary and Holdridge Plots

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-PlotTools >= 0.2.0
BuildRequires:    R-CRAN-RcppHungarian 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-PlotTools >= 0.2.0
Requires:         R-CRAN-RcppHungarian 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-sp 

%description
Plots ternary diagrams (simplex plots / Gibbs triangles) and Holdridge
life zone plots <doi:10.1126/science.105.2727.367> using the standard
graphics functions. Allows custom annotation, interpolating, contouring
and scaling of plotting region. Includes a 'Shiny' user interface for
point-and-click ternary plotting. An alternative to 'ggtern', which uses
the 'ggplot2' family of plotting functions.

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
