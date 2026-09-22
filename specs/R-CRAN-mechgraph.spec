%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mechgraph
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Mechanism Evidence Graph Data Model

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-igraph 

%description
Provides a lightweight graph data model for representing, combining,
querying, and summarizing evidence-backed biological mechanism graphs. A
mechgraph is an S3 list holding a node table, an edge table, and
provenance metadata. The package implements builders that convert STRING
and BioGRID interaction tables into mechgraph objects, combiners
(mg_bind(), mg_combine()) that merge graphs while preserving duplicate
evidence records, accessors (mg_nodes(), mg_edges(), mg_metadata()) and
mutators (mg_add_*(), mg_drop_*()) for node and edge tables, filters by
type, source, identifier, and score, induced-subgraph construction,
structural validation (mg_validate()), and quality-control summaries
(mg_qc()). Szklarczyk et al. (2023) <doi:10.1093/nar/gkac1000> Oughtred et
al. (2021) <doi:10.1002/pro.3938>.

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
