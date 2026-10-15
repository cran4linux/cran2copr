%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dynamicmultiplex
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tracking Communities in Changing Temporal Networks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph >= 2.0.0
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-igraph >= 2.0.0
Requires:         R-CRAN-clue 
Requires:         R-CRAN-rlang 

%description
Tools for temporal networks that change over time, where nodes enter and
leave, groups form, split, merge and dissolve, and periods differ in size.
The temporal fitters track nodes and communities across periods. A
community keeps one identifier while it persists, and a newly formed group
receives a new one. Two-stage fitters run Louvain or Leiden community
detection in each period and link communities in linked periods by Jaccard
similarity, the overlap coefficient or node-strength weighted variants.
The 'layer_links' argument sets which periods are directly linked,
adjacent periods only by default. By default all periods are fitted
jointly, so later periods can change earlier labels, and tracking =
'filtered' prevents this. Multislice modularity (Mucha et al. 2010)
<doi:10.1126/science.1184819> and Hungarian matching are included as
comparison methods, and a bootstrap stability score helps choose between
the two-stage and multislice approaches.

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
