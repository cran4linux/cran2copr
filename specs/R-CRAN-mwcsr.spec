%global __brp_check_rpaths %{nil}
%global packname  mwcsr
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Solvers for Maximum Weight Connected Subgraph Problem and Its Variants

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-Rcpp 

%description
Algorithms for solving various Maximum Weight Connected Subgraph Problems,
including variants with budget constraints, cardinality constraints,
weighted edges and signals. The package represents an R interface to
high-efficient solvers based on relax-and-cut approach (Álvarez-Miranda
E., Sinnl M. (2017) <doi:10.1016/j.cor.2017.05.015>) mixed-integer
programming (Loboda A., Artyomov M., and Sergushichev A. (2016)
<doi:10.1007/978-3-319-43681-4_17>) and simulated annealing.

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
