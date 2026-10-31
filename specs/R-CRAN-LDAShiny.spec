%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LDAShiny
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Shiny Application for Topic Modeling of Scientific Literature

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-beepr 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-config 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-golem 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-LDAvis 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-quanteda 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinybusy 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-slam 
BuildRequires:    R-CRAN-SnowballC 
BuildRequires:    R-CRAN-stopwords 
BuildRequires:    R-CRAN-textmineR 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-wordcloud 
Requires:         R-CRAN-beepr 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-config 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-golem 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-LDAvis 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-quanteda 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinybusy 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-slam 
Requires:         R-CRAN-SnowballC 
Requires:         R-CRAN-stopwords 
Requires:         R-CRAN-textmineR 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tm 
Requires:         R-utils 
Requires:         R-CRAN-wordcloud 

%description
A 'shiny' application that guides users through an exploratory review of
scientific literature using Latent Dirichlet Allocation (LDA) topic
modeling. It imports bibliometric records exported from databases such as
'Scopus' and 'Web of Science', performs text preprocessing, helps select
the number of topics, fits the final model, and visualizes the results and
the evolution of topics over time. The methodology is described in De la
Hoz-M et al. (2021) <doi:10.3390/math9141671>.

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
