%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  easypaper
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Automate Reproducible 'Quarto' Manuscripts Ready for Submission

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-dataspice 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-here 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-quarto 
BuildRequires:    R-CRAN-ragg 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-renv 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-zip 
Requires:         R-CRAN-dataspice 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-here 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-quarto 
Requires:         R-CRAN-ragg 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-renv 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-rstudioapi 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-zip 

%description
Creates and builds reproducible scientific manuscripts written in
'Quarto'. create_paper() writes a project that holds only the paper: its
sections as separate files, its references and journal style as a CSL
(Citation Style Language) file, the setup of the analysis and the data.
The functions of the package then render it for any journal, check
citations and cross-references before every render, export figures to PNG,
JPEG and TIFF at 600 dpi, give the supplementary material a document and a
bibliography of its own, and build the submission folder: the manuscript
split for double-blind review, together with a data and code compendium
ready for a data repository. Every render records the versions of the
packages it used, 'easypaper' included, with 'renv', so the manuscript can
be rebuilt years later. Every render also sets the scientific names of the
reference list in italics, checking genera and species against the Global
Biodiversity Information Facility (GBIF) Backbone Taxonomy
<doi:10.15468/39omei>; italicize_species() does the same for any other
bibliography.

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
