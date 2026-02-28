%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RcppTskit
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          'R' Access to the 'tskit C' API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-reticulate >= 1.43.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.8
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-reticulate >= 1.43.0
Requires:         R-CRAN-Rcpp >= 1.0.8
Requires:         R-methods 
Requires:         R-CRAN-R6 

%description
'Tskit' enables efficient storage, manipulation, and analysis of ancestral
recombination graphs (ARGs) using succinct tree sequence encoding. The
tree sequence encoding of an ARG is described in Wong et al. (2024)
<doi:10.1093/genetics/iyae100>, while `tskit` project is described in
Jeffrey et al. (2026) <doi:10.48550/arXiv.2602.09649>. See also
<https://tskit.dev> for project news, documentation, and tutorials.
'Tskit' provides 'Python', 'C', and 'Rust' application programming
interfaces (APIs). The 'Python' API can be called from 'R' via the
'reticulate' package to load and analyse tree sequences as described at
<https://tskit.dev/tutorials/tskitr.html>. 'RcppTskit' provides 'R' access
to the 'tskit C' API for cases where the 'reticulate' option is not
optimal; for example, high-performance or low-level work with tree
sequences. Currently, 'RcppTskit' provides a limited set of 'R' functions
because the 'Python' API and 'reticulate' already covers most needs.

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
