%global __brp_check_rpaths %{nil}
%global packname  interplex
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Coercion Methods for Simplicial Complex Data Structures

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Computational topology, which includes topological data analysis (TDA),
makes pervasive use of abstract mathematical objects called simplicial
complexes; see Edelsbrunner and Harer (2010) <doi:10.1090/mbk/069>.
Several R packages and other software libraries used through an R
interface construct and use data structures that represent simplicial
complexes, including mathematical graphs viewed as 1-dimensional
complexes. This package provides coercers (converters) between these data
structures. Currently supported structures are complete lists of simplices
as used by 'TDA'; the simplex trees of Boissonnat and Maria (2014)
<doi:10.1007/s00453-014-9887-3> as implemented in 'simplextree' and in
Python GUDHI (by way of 'reticulate'); and the graph classes of 'igraph'
and 'network', by way of the 'intergraph' package.

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
