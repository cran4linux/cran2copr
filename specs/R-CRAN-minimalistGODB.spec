%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  minimalistGODB
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Build a Minimalist Gene Ontology (GO) Database (GODB)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch

%description
Normally building a GODB is fairly complicated, involving downloading
multiple database files and using these to build e.g. a 'mySQL' database.
Accessing this database is also complicated, involving an intimate
knowledge of the database in order to construct reliable queries. Here we
have a more modest goal, generating GOGOA3, which is a stripped down
version of the GODB that was originally restricted to human genes as
designated by the HUGO Gene Nomenclature Committee (HGNC) (see
<https://geneontology.org/>). I have now added about two dozen additional
species, namely all species represented on the Gene Ontology download page
<https://current.geneontology.org/products/pages/downloads.html>. This
covers most of the model organisms that are commonly used in bio-medical
and basic research (assuming that anyone still has a grant to do such
research). This can be built in a matter of seconds from 2 easily
downloaded files (see
<https://current.geneontology.org/products/pages/downloads.html> and
<https://geneontology.org/docs/download-ontology/>), and it can be queried
by e.g. w<-which(GOGOA3[,"HGNC"] %%in%% hgncList) where GOGOA3 is a matrix
representing the minimalist GODB and hgncList is a list of gene
identifiers. This database will be used in my upcoming package 'GoMiner'
which is based on my previous publication (see Zeeberg, B.R., Feng, W.,
Wang, G. et al. (2003)<doi:10.1186/gb-2003-4-4-r28>). Relevant .RData
files are available from GitHub
(<https://github.com/barryzee/GO/tree/main/databases>).

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
