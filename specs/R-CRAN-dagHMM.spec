%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dagHMM
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Directed Acyclic Graph HMM with TAN Structured Emissions

License:          GPL (>= 2.0.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-PRROC 
BuildRequires:    R-CRAN-bnlearn 
BuildRequires:    R-CRAN-bnclassify 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-future 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-PRROC 
Requires:         R-CRAN-bnlearn 
Requires:         R-CRAN-bnclassify 

%description
Hidden Markov models (HMMs) are a formal foundation for making
probabilistic models of linear sequence. They provide a conceptual toolkit
for building complex models just by drawing an intuitive picture. They are
at the heart of a diverse range of programs, including genefinding,
profile searches, multiple sequence alignment and regulatory site
identification. HMMs are the Legos of computational sequence analysis. In
graph theory, a tree is an undirected graph in which any two vertices are
connected by exactly one path, or equivalently a connected acyclic
undirected graph. Tree represents the nodes connected by edges. It is a
non-linear data structure. A poly-tree is simply a directed acyclic graph
whose underlying undirected graph is a tree. The model proposed in this
package is the same as an HMM but where the states are linked via a
polytree structure rather than a simple path.

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
