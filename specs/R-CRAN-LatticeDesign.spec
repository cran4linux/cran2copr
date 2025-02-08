%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LatticeDesign
%global packver   3.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Lattice-Based Space-Filling Designs

License:          LGPL-2.1
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-methods 
Requires:         R-methods 

%description
Lattice-based space-filling designs with fill or separation distance
properties including interleaved lattice-based minimax distance designs
proposed in Xu He (2017) <doi:10.1093/biomet/asx036>, interleaved
lattice-based maximin distance designs proposed in Xu He (2018)
<doi:10.1093/biomet/asy069>, interleaved lattice-based designs with low
fill and high separation distance properties proposed in Xu He (2024)
<doi:10.1137/23M156940X>, rotated sphere packing designs proposed in Xu He
(2017) <doi:10.1080/01621459.2016.1222289>, sliced rotated sphere packing
designs proposed in Xu He (2019) <doi:10.1080/00401706.2018.1458655>, and
densest packing-based maximum projections designs proposed in Xu He (2021)
<doi:10.1093/biomet/asaa057> and Xu He (2018)
<doi:10.48550/arXiv.1709.02062>.

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
