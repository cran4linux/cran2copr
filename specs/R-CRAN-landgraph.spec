%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  landgraph
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Graphs and Covariance for Landscape Genetics

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Shared, dependency-light primitives for landscape-genetic network methods:
a lightweight deme/landscape graph (vertex coordinates and an undirected
edge list) with constructors from coordinates; genetic covariance and
distance from biallelic or multiallelic data (the normalized-dosage
covariance of Yang et al. (2010) <doi:10.1038/ng.608>, and the
multivariate covariance of Dyer and Nason (2004)
<doi:10.1111/j.1365-294X.2004.02177.x> built by the Gower (1966)
<doi:10.1093/biomet/53.3-4.325> double-centering); pairwise F_ST by the
estimator of Bhatia et al. (2013) <doi:10.1101/gr.154831.113>; and
antisymmetric per-edge directional covariate builders (the gradient of a
scalar potential, and the projection of a vector flow field). Used by
'terradish' (symmetric resistance).

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
