%global __brp_check_rpaths %{nil}
%global packname  miRetrieve
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          miRNA Text Mining in Abstracts

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.9.4.1
BuildRequires:    R-CRAN-openxlsx >= 4.2.4
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-wordcloud >= 2.6
BuildRequires:    R-CRAN-magrittr >= 2.0.1
BuildRequires:    R-CRAN-zoo >= 1.8.9
BuildRequires:    R-CRAN-readr >= 1.4.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-xml2 >= 1.3.2
BuildRequires:    R-CRAN-readxl >= 1.3.1
BuildRequires:    R-CRAN-tidyr >= 1.1.3
BuildRequires:    R-CRAN-scales >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 1.0.7
BuildRequires:    R-CRAN-textclean >= 0.9.3
BuildRequires:    R-CRAN-forcats >= 0.5.1
BuildRequires:    R-CRAN-rlang >= 0.4.11
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-tidytext >= 0.3.1
BuildRequires:    R-CRAN-topicmodels >= 0.2.12
Requires:         R-CRAN-plotly >= 4.9.4.1
Requires:         R-CRAN-openxlsx >= 4.2.4
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-wordcloud >= 2.6
Requires:         R-CRAN-magrittr >= 2.0.1
Requires:         R-CRAN-zoo >= 1.8.9
Requires:         R-CRAN-readr >= 1.4.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-xml2 >= 1.3.2
Requires:         R-CRAN-readxl >= 1.3.1
Requires:         R-CRAN-tidyr >= 1.1.3
Requires:         R-CRAN-scales >= 1.1.1
Requires:         R-CRAN-dplyr >= 1.0.7
Requires:         R-CRAN-textclean >= 0.9.3
Requires:         R-CRAN-forcats >= 0.5.1
Requires:         R-CRAN-rlang >= 0.4.11
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-tidytext >= 0.3.1
Requires:         R-CRAN-topicmodels >= 0.2.12

%description
Providing tools for microRNA (miRNA) text mining. miRetrieve summarizes
miRNA literature by extracting, counting, and analyzing miRNA names, thus
aiming at gaining biological insights into a large amount of text within a
short period of time. To do so, miRetrieve uses regular expressions to
extract miRNAs and tokenization to identify meaningful miRNA associations.
In addition, miRetrieve uses the latest miRTarBase version 8.0 (Hsi-Yuan
Huang et al. (2020) "miRTarBase 2020: updates to the experimentally
validated microRNA–target interaction database" <doi:10.1093/nar/gkz896>)
to display field-specific miRNA-mRNA interactions. The most important
functions are available as a Shiny web application under
<https://miretrieve.shinyapps.io/miRetrieve/>.

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
