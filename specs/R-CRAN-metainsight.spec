%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  metainsight
%global packver   7.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          7.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A 'shiny' Application for Network Meta-Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-meta >= 8.1.0
BuildRequires:    R-CRAN-netmeta >= 3.1.0
BuildRequires:    R-CRAN-mirai >= 2.0.0
BuildRequires:    R-CRAN-shiny >= 1.8.1
BuildRequires:    R-CRAN-bnma >= 1.4.0
BuildRequires:    R-CRAN-gemtc >= 1.1.1
BuildRequires:    R-CRAN-shinyWidgets >= 0.6.0
BuildRequires:    R-CRAN-DT >= 0.5
BuildRequires:    R-CRAN-bayesplot 
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-cookies 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-gargoyle 
BuildRequires:    R-CRAN-ggiraphExtra 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-gt 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-knitcitations 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-MCMCvis 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-quarto 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rio 
BuildRequires:    R-CRAN-rintrojs 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-rsvg 
BuildRequires:    R-CRAN-shinyalert 
BuildRequires:    R-CRAN-shinybusy 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-svglite 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-meta >= 8.1.0
Requires:         R-CRAN-netmeta >= 3.1.0
Requires:         R-CRAN-mirai >= 2.0.0
Requires:         R-CRAN-shiny >= 1.8.1
Requires:         R-CRAN-bnma >= 1.4.0
Requires:         R-CRAN-gemtc >= 1.1.1
Requires:         R-CRAN-shinyWidgets >= 0.6.0
Requires:         R-CRAN-DT >= 0.5
Requires:         R-CRAN-bayesplot 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-cookies 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-gargoyle 
Requires:         R-CRAN-ggiraphExtra 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-gt 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-knitcitations 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-MCMCvis 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-quarto 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rio 
Requires:         R-CRAN-rintrojs 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-rsvg 
Requires:         R-CRAN-shinyalert 
Requires:         R-CRAN-shinybusy 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-svglite 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-xml2 

%description
Conduct network meta-analyses through a graphical user interface using
'bnma', 'gemtc' and 'netmeta' with additional analysis provided by 'meta'
and 'metafor'. Frequentist, Bayesian, meta-regression and baseline risk
meta-regression analyses can all be conducted using a consistent data
structure and terminology. Many options are provided for downloading
publication-ready outputs and analyses can be reproduced outside of the
application by downloading a 'quarto' file. The interface was generated
using 'shinyscholar'. The initial version of the app was described by Owen
et al. (2018) <doi:10.1002/jrsm.1373>, Bayesian ranking visualisations
were described by Nevill et al. (2023)
<doi:10.1016/j.jclinepi.2023.02.016> and metaregression was described by
Morris et al. (2025) <doi:10.1016/j.jclinepi.2025.111839>.

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
