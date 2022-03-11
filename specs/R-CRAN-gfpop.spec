%global __brp_check_rpaths %{nil}
%global packname  gfpop
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Graph-Constrained Functional Pruning Optimal Partitioning

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-Rcpp >= 1.0.0

%description
Penalized parametric change-point detection by functional pruning dynamic
programming algorithm. The successive means are constrained using a graph
structure with edges defining the nature of the changes These changes can
be unconstrained (type std), up or down constrained (type up and down) or
constrained by a minimal size jump (type abs). The type null means that
the graph allows us to stay on the same segment. To each edge we can
associate some additional properties: a minimal gap size, a penalty, some
robust parameters (K,a) for biweight (K) and Huber losses (K and a). The
user can also constrain the inferred means to lie between some minimal and
maximal values. Data is modeled by a cost with possible use of a robust
loss, biweight and Huber (see edge parameters K and a). These costs should
have a quadratic, log-linear or a log-log representation.

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
