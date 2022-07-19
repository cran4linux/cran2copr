%global __brp_check_rpaths %{nil}
%global packname  LDABiplots
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Biplot Graphical Interface for LDA Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-shinyalert 
BuildRequires:    R-CRAN-shinybusy 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-highcharter 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-SnowballC 
BuildRequires:    R-CRAN-ldatuning 
BuildRequires:    R-CRAN-topicmodels 
BuildRequires:    R-CRAN-textmineR 
BuildRequires:    R-CRAN-chinese.misc 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-textplot 
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-factoextra 
BuildRequires:    R-CRAN-quanteda 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-shinyalert 
Requires:         R-CRAN-shinybusy 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-highcharter 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-SnowballC 
Requires:         R-CRAN-ldatuning 
Requires:         R-CRAN-topicmodels 
Requires:         R-CRAN-textmineR 
Requires:         R-CRAN-chinese.misc 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-textplot 
Requires:         R-CRAN-glasso 
Requires:         R-CRAN-qgraph 
Requires:         R-CRAN-Matrix 
Requires:         R-utils 
Requires:         R-CRAN-factoextra 
Requires:         R-CRAN-quanteda 

%description
Contains the development of a tool that provides a web-based graphical
user interface (GUI) to perform Biplots representations from a scraping of
news from digital newspapers under the Bayesian approach of Latent
Dirichlet Assignment (LDA) and machine learning algorithms. Contains LDA
methods described by Blei , David M., Andrew Y. Ng and Michael I. Jordan
(2003) <https://jmlr.org/papers/volume3/blei03a/blei03a.pdf>, and Biplot
methods described by Gabriel K.R(1971) <doi:10.1093/biomet/58.3.453> and
Galindo-Villardon P(1986)
<https://diarium.usal.es/pgalindo/files/2012/07/Questiio.pdf>.

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
