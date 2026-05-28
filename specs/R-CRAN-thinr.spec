%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  thinr
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Binary Image Thinning Algorithms

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-Rcpp 

%description
Thinning (skeletonization) algorithms for binary raster images. Provides
seven algorithms behind a single dispatching function: Zhang-Suen (Zhang
and Suen 1984) <doi:10.1145/357994.358023>, Guo-Hall (Guo and Hall 1989)
<doi:10.1145/62065.62074>, a 2-D adaptation of Lee (Lee, Kashyap, and Chu
1994) <doi:10.1006/cgip.1994.1042>, K3M (Saeed, Tabedzki, Rybnik, and
Adamski 2010) <doi:10.2478/v10006-010-0024-4>, the parallel form commonly
attributed to Hilditch (1969, in 'Machine Intelligence 4'), OPTA / SPTA
(Naccache and Shinghal 1984), and Holt and colleagues (1987)
<doi:10.1145/12527.12531>. Also provides the medial axis transform (Blum
1967) and a distance transform implementation following Felzenszwalb and
Huttenlocher (2012) <doi:10.4086/toc.2012.v008a019>. The drop-in
thinImage() matches the signature of thinImage() in the 'EBImage' package
on Bioconductor so existing code can switch parsers without changes. The
wider thin() API selects the algorithm by name.

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
