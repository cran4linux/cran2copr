%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  annsearchR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Approximate Nearest Neighbour Search

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-stats 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-lifecycle 
Requires:         R-methods 
Requires:         R-CRAN-R6 
Requires:         R-stats 

%description
R interface to the Rust crate 'ann-search-rs'. Build an exact or
approximate nearest neighbour index once, keep it in memory behind an 'R6'
object and query it as often as you like. Index types include hierarchical
navigable small world graphs (HNSW), 'Annoy' random projection trees,
inverted file indices (IVF), nearest neighbour descent (NNDescent) and
'Vamana' graphs. Multi-threaded via the Rust crate 'Rayon', with 32-bit or
64-bit floating point storage. Methods are described in Malkov and
Yashunin (2020) <doi:10.1109/TPAMI.2018.2889473> and Dong et al. (2011)
<doi:10.1145/1963405.1963487>.

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
