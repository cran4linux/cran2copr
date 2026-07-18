%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hood2net
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Create a Language Network from Neighborhoods of Words

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-stringdist 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-stringdist 

%description
Input a list of words and/or their phonological transcriptions and this
package creates a language network based on their neighborhood structure.
First, the phonological/orthographic neighbors for each item in the list
are identified based on various definitions of a neighbor (e.g.,
edit-distance (substitution, deletion, or addition), substitution-only;
distance size (1-edit or more); based on single characters or segments
indicated by separators) and summarizes this information in an 'igraph'
network object for subsequent analyses. For more details see Luce & Pisoni
(1998) <doi:10.1097/00003446-199802000-00001> and Vitevitch (2008)
<doi:10.1044/1092-4388(2008/030)>. Helper functions for extracting network
metrics, neighbors, and other information from the language network are
provided. This package is intended for psycholinguists interested in
modeling language networks and word neighborhoods in various languages.

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
