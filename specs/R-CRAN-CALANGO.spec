%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CALANGO
%global packver   1.0.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.12
Release:          1%{?dist}%{?buildtag}
Summary:          Comparative Analysis with Annotation-Based Genomic Components

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape >= 5.3.0
BuildRequires:    R-CRAN-plotly >= 4.9.2
BuildRequires:    R-CRAN-nlme >= 3.1.0
BuildRequires:    R-CRAN-ggplot2 >= 2.3.2
BuildRequires:    R-CRAN-rmarkdown >= 2.1
BuildRequires:    R-CRAN-htmlwidgets >= 1.5.1
BuildRequires:    R-CRAN-pkgdown >= 1.5.1
BuildRequires:    R-CRAN-pbmcapply >= 1.5.0
BuildRequires:    R-CRAN-BiocManager >= 1.30.10
BuildRequires:    R-CRAN-knitr >= 1.28
BuildRequires:    R-CRAN-dendextend >= 1.15.2
BuildRequires:    R-CRAN-heatmaply >= 1.1.0
BuildRequires:    R-CRAN-taxize >= 0.9.92
BuildRequires:    R-CRAN-htmltools >= 0.5.0
BuildRequires:    R-CRAN-assertthat >= 0.2.1
BuildRequires:    R-CRAN-DT >= 0.13
Requires:         R-CRAN-ape >= 5.3.0
Requires:         R-CRAN-plotly >= 4.9.2
Requires:         R-CRAN-nlme >= 3.1.0
Requires:         R-CRAN-ggplot2 >= 2.3.2
Requires:         R-CRAN-rmarkdown >= 2.1
Requires:         R-CRAN-htmlwidgets >= 1.5.1
Requires:         R-CRAN-pkgdown >= 1.5.1
Requires:         R-CRAN-pbmcapply >= 1.5.0
Requires:         R-CRAN-BiocManager >= 1.30.10
Requires:         R-CRAN-knitr >= 1.28
Requires:         R-CRAN-dendextend >= 1.15.2
Requires:         R-CRAN-heatmaply >= 1.1.0
Requires:         R-CRAN-taxize >= 0.9.92
Requires:         R-CRAN-htmltools >= 0.5.0
Requires:         R-CRAN-assertthat >= 0.2.1
Requires:         R-CRAN-DT >= 0.13

%description
A first-principle, phylogeny-aware comparative genomics tool for
investigating associations between terms used to annotate genomic
components (e.g., Pfam IDs, Gene Ontology terms,) with quantitative or
rank variables such as number of cell types, genome size, or density of
specific genomic elements. See the project website for more information,
documentation and examples.

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
