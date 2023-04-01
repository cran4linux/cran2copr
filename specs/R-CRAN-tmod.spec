%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tmod
%global packver   0.50.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.50.13
Release:          1%{?dist}%{?buildtag}
Summary:          Feature Set Enrichment Analysis for Metabolomics and Transcriptomics

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-beeswarm 
BuildRequires:    R-CRAN-tagcloud 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plotwidgets 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-pheatmap 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-ggrepel 
Requires:         R-CRAN-beeswarm 
Requires:         R-CRAN-tagcloud 
Requires:         R-CRAN-XML 
Requires:         R-methods 
Requires:         R-CRAN-plotwidgets 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-pheatmap 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-ggrepel 

%description
Methods and feature set definitions for feature or gene set enrichment
analysis in transcriptional and metabolic profiling data. Package includes
tests for enrichment based on ranked lists of features, functions for
visualisation and multivariate functional analysis. See Zyla et al (2019)
<doi:10.1093/bioinformatics/btz447>.

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
