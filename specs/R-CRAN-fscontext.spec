%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fscontext
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          File System Contextualisation and Record Set Reconstruction

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-dataset 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-labelled 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-dplyr 
Requires:         R-utils 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-dataset 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-labelled 
Requires:         R-CRAN-jsonlite 

%description
Provides a provenance-aware framework for contextual reconstruction from
file systems and related digital resource collections. The package creates
reproducible snapshots of file-level metadata, paths, repository context,
and optional content signatures. It supports contextual grouping,
structural abstraction, temporal analysis, semantic stabilization,
duplicate and reuse detection, and lightweight workflow reconstruction
from file system observations. The framework deliberately separates
observational evidence, contextual abstraction, semantic interpretation,
and analytical reconstruction, enabling reproducible workflows that can be
inspected by reviewers. It is designed to support future alignment with
archival and contextual knowledge representation models, including the
World Wide Web Consortium Provenance Ontology (PROV-O): Lebo et al. (2013)
<https://www.w3.org/TR/prov-o/> and Records in Contexts developed by the
International Council on Archives Expert Group on Archival Description
(EGAD)
<https://www.ica.org/ica-network/expert-groups/egad/records-in-contexts-ric/>.

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
