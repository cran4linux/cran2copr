%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rbiom
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Read/Write, Analyze, and Visualize 'BIOM' Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-fillpattern 
BuildRequires:    R-CRAN-ggbeeswarm 
BuildRequires:    R-CRAN-ggnewscale 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-ggtext 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-parallelly 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-pillar 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-slam 
BuildRequires:    R-CRAN-vegan 
Requires:         R-methods 
Requires:         R-CRAN-mgcv 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-fillpattern 
Requires:         R-CRAN-ggbeeswarm 
Requires:         R-CRAN-ggnewscale 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-ggtext 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-parallelly 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-pillar 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-slam 
Requires:         R-CRAN-vegan 

%description
A toolkit for working with Biological Observation Matrix ('BIOM') files.
Read/write all 'BIOM' formats. Compute rarefaction, alpha diversity, and
beta diversity (including 'UniFrac'). Summarize counts by taxonomic level.
Subset based on metadata. Generate visualizations and statistical
analyses. CPU intensive operations are coded in C for speed.

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
