%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  theaitetos
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Ancient Intelligence Geometric Superposition Field Calculations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-ggplot2 

%description
Establishes a deterministic geometric extension framework within the
'theaitetos' package, honoring the ancient mathematical foundations of
Theaetetus of Athens (400 BC). Incorporates the stereometric proofs on the
regular octahedron later recorded in Plato (ca. 369 BC) "Theaetetus"
<urn:cts:greekLit:tlg0059.tlg006> and Euclid (ca. 300 BC) "Elements"
<urn:cts:greekLit:tlg1799.tlg001>. References the standard Greek text
tradition by Heiberg (1885) "Euclidis Elementa" and the analytical
translations by Heath (1926) "The Thirteen Books of Euclid's Elements". To
achieve operational utility, the architecture delivers a high-level
computational core engine that abstracts complex 3D-to-2D vector
projections and scalar wave superpositions, eliminating low-level
reprogramming. It integrates a standardized visualization layer built upon
'ggplot2' to render high-resolution continuous scalar fields and provides
a runtime-configurable selection interface across multiple physical and
biological dimensions. Operates under the modern paradigm of a
hypothetical holographic universe by referencing the foundational concepts
of 't Hooft (1993) <doi:10.48550/arXiv.gr-qc/9310026> and Susskind (1995)
<doi:10.1063/1.531249> to project Euclidean invariants onto a
lower-dimensional boundary plane. Serves as a creative epistemological
sub-module utilizing the core analytical computations of the 'octawave'
package.

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
