%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ETRep
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Elliptical Tubes Under the Relative Curvature Condition

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-shapes 
BuildRequires:    R-CRAN-Morpho 
BuildRequires:    R-CRAN-matlib 
BuildRequires:    R-CRAN-RSpincalc 
BuildRequires:    R-CRAN-rotations 
BuildRequires:    R-CRAN-Rvcg 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-htmlwidgets 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-shapes 
Requires:         R-CRAN-Morpho 
Requires:         R-CRAN-matlib 
Requires:         R-CRAN-RSpincalc 
Requires:         R-CRAN-rotations 
Requires:         R-CRAN-Rvcg 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-htmlwidgets 

%description
Analysis of elliptical tubes with applications in biological modeling. The
package is based on the references: Taheri, M., Pizer, S. M., & Schulz, J.
(2024) "The Mean Shape under the Relative Curvature Condition." Journal of
Computational and Graphical Statistics <doi:10.1080/10618600.2025.2535600>
and arXiv <doi:10.48550/arXiv.2404.01043>. Mohsen Taheri Shalmani (2024)
"Shape Statistics via Skeletal Structures", PhD Thesis, University of
Stavanger, Norway <doi:10.13140/RG.2.2.34500.23685>. Key features include
constructing discrete elliptical tubes, calculating transformations,
validating structures under the Relative Curvature Condition (RCC),
computing means, and generating simulations. Supports intrinsic and
non-intrinsic mean calculations and transformations, size estimation,
plotting, and random sample generation based on a reference tube. The
intrinsic approach relies on the interior path of the original non-convex
space, incorporating the RCC, while the non-intrinsic approach uses a
basic robotic arm transformation that disregards the RCC.

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
