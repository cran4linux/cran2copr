%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  kuzuR
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to 'kuzu' Graph Database

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidygraph 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidygraph 

%description
Provides a high-performance 'R' interface to the 'kuzu' graph database. It
uses the 'reticulate' package to wrap the official 'Python' client
('kuzu', 'pandas', and 'networkx'), allowing users to interact with 'kuzu'
seamlessly from within 'R'. Key features include managing database
connections, executing 'Cypher' queries, and efficiently loading data from
'R' data frames. It also provides seamless integration with the 'R'
ecosystem by converting query results directly into popular 'R' data
structures, including 'tibble', 'igraph', 'tidygraph', and 'g6R' objects,
making 'kuzu's powerful graph computation capabilities readily available
for data analysis and visualization workflows in 'R'. The 'kuzu'
documentation can be found at <https://kuzudb.github.io/docs/>.

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
