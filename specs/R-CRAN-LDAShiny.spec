%global packname  LDAShiny
%global packver   0.9.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.3
Release:          1%{?dist}%{?buildtag}
Summary:          User-Friendly Interface for Review of Scientific Literature

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-DT >= 0.15
BuildRequires:    R-CRAN-beepr 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-chinese.misc 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-highcharter 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-ldatuning 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-quanteda 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyalert 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-SnowballC 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-textmineR 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidytext 
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-CRAN-topicmodels 
Requires:         R-CRAN-DT >= 0.15
Requires:         R-CRAN-beepr 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-chinese.misc 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-highcharter 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-ldatuning 
Requires:         R-parallel 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-quanteda 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyalert 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-SnowballC 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-textmineR 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidytext 
Requires:         R-CRAN-tm 
Requires:         R-CRAN-topicmodels 

%description
Contains the development of a tool that provides a web-based graphical
user interface (GUI) to perform a review of the scientific literature
under the Bayesian approach of Latent Dirichlet Allocation (LDA)and
machine learning algorithms. The application methodology is framed by the
well known procedures in topic modelling on how to clean and process data.
Contains methods described by Blei, David M., Andrew Y. Ng, and Michael I.
Jordan (2003) <https://jmlr.org/papers/volume3/blei03a/blei03a.pdf>
Allocation"; Thomas L. Griffiths and Mark Steyvers (2004)
<doi:10.1073/pnas.0307752101> ; Xiong Hui, et al (2019)
<doi:10.1016/j.cie.2019.06.010>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
