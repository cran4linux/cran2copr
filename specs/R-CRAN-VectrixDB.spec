%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  VectrixDB
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Lightweight Vector Database with Embedded Machine Learning Models

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-text2vec >= 0.6.0
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-stopwords 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-DBI 
Requires:         R-CRAN-text2vec >= 0.6.0
Requires:         R-CRAN-R6 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-stopwords 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-DBI 

%description
A lightweight vector database for text retrieval in R with embedded
machine learning models and no external API (Application Programming
Interface) keys. Supports dense and hybrid search, optional HNSW
(Hierarchical Navigable Small World) approximate nearest-neighbor
indexing, faceted filters with ACL (Access Control List) metadata,
command-line tools, and a local dashboard built with 'shiny'. The HNSW
method is described by Malkov and Yashunin (2018)
<doi:10.1109/TPAMI.2018.2889473>.

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
