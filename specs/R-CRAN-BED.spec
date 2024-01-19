%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BED
%global packver   1.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Biological Entity Dictionary (BED)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-neo2R >= 2.4.1
BuildRequires:    R-CRAN-rstudioapi >= 0.5
BuildRequires:    R-CRAN-shiny >= 0.13
BuildRequires:    R-CRAN-miniUI >= 0.1.1
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-DT 
Requires:         R-CRAN-neo2R >= 2.4.1
Requires:         R-CRAN-rstudioapi >= 0.5
Requires:         R-CRAN-shiny >= 0.13
Requires:         R-CRAN-miniUI >= 0.1.1
Requires:         R-CRAN-visNetwork 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-stringr 
Requires:         R-utils 
Requires:         R-CRAN-DT 

%description
An interface for the 'Neo4j' database providing mapping between different
identifiers of biological entities. This Biological Entity Dictionary
(BED) has been developed to address three main challenges. The first one
is related to the completeness of identifier mappings. Indeed, direct
mapping information provided by the different systems are not always
complete and can be enriched by mappings provided by other resources. More
interestingly, direct mappings not identified by any of these resources
can be indirectly inferred by using mappings to a third reference. For
example, many human Ensembl gene ID are not directly mapped to any Entrez
gene ID but such mappings can be inferred using respective mappings to
HGNC ID. The second challenge is related to the mapping of deprecated
identifiers. Indeed, entity identifiers can change from one resource
release to another. The identifier history is provided by some resources,
such as Ensembl or the NCBI, but it is generally not used by mapping
tools. The third challenge is related to the automation of the mapping
process according to the relationships between the biological entities of
interest. Indeed, mapping between gene and protein ID scopes should not be
done the same way than between two scopes regarding gene ID. Also,
converting identifiers from different organisms should be possible using
gene orthologs information. The method has been published by Godard and
van Eyll (2018) <doi:10.12688/f1000research.13925.3>.

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
