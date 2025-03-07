%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rollupTree
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Perform Recursive Computations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-igraph 

%description
Mass rollup for a Bill of Materials is an example of a class of
computations in which elements are arranged in a tree structure and some
property of each element is a computed function of the corresponding
values of its child elements. Leaf elements, i.e., those with no children,
have values assigned. In many cases, the combining function is simple
arithmetic sum; in other cases (e.g., mass properties), the combiner may
involve other information such as the geometric relationship between
parent and child, or statistical relations such as root-sum-of-squares
(RSS). This package implements a general function for such problems. It is
adapted to specific recursive computations by functional programming
techniques; the caller passes a function as the update parameter to
rollup() (or, at a lower level, passes functions as the get, set, combine,
and override parameters to update_prop()) at runtime to specify the
desired operations. The implementation relies on graph-theoretic
algorithms from the 'igraph' package of Csárdi, et al. (2006
<doi:10.5281/zenodo.7682609>).

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
