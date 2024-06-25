%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FAIRmaterials
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Ontology Tools with Data FAIRification in Development

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rdflib 
BuildRequires:    R-CRAN-jsonld 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-DiagrammeR 
BuildRequires:    R-CRAN-DiagrammeRsvg 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-readr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rdflib 
Requires:         R-CRAN-jsonld 
Requires:         R-CRAN-httr 
Requires:         R-utils 
Requires:         R-CRAN-DiagrammeR 
Requires:         R-CRAN-DiagrammeRsvg 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-readr 

%description
Translates several CSV files with ontological terms and corresponding data
into RDF triples. These RDF triples are stored in OWL and JSON-LD files,
facilitating data accessibility, interoperability, and knowledge
unification. The triples are also visualized in a graph saved as an SVG.
The input CSVs must be formatted with a template from a public Google
Sheet; see README or vignette for more information. This is a tool is used
by the SDLE Research Center at Case Western Reserve University to create
and visualize material science ontologies, and it includes example
ontologies to demonstrate its capabilities. This work was supported by the
U.S. Department of Energy’s Office of Energy Efficiency and Renewable
Energy (EERE) under Solar Energy Technologies Office (SETO) Agreement
Numbers E-EE0009353 and DE-EE0009347, Department of Energy (National
Nuclear Security Administration) under Award Number DE-NA0004104 and
Contract number B647887, and U.S. National Science Foundation Award under
Award Number 2133576.

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
