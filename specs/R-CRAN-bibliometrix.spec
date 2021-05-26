%global packname  bibliometrix
%global packver   3.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Comprehensive Science Mapping Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-bibliometrixData 
BuildRequires:    R-CRAN-dimensionsR 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-factoextra 
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-ggnetwork 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-pubmedR 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-rscopus 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-SnowballC 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidytext 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-CRAN-bibliometrixData 
Requires:         R-CRAN-dimensionsR 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-factoextra 
Requires:         R-CRAN-FactoMineR 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-ggnetwork 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-pubmedR 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-rscopus 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-SnowballC 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidytext 

%description
Tool for quantitative research in scientometrics and bibliometrics. It
provides various routines for importing bibliographic data from 'SCOPUS'
(<https://scopus.com>), 'Clarivate Analytics Web of Science'
(<https://www.webofknowledge.com/>), 'Digital Science Dimensions'
(<https://www.dimensions.ai/>), 'Cochrane Library'
(<https://www.cochranelibrary.com/>), 'Lens' (<https://lens.org>), and
'PubMed' (<https://pubmed.ncbi.nlm.nih.gov/>) databases, performing
bibliometric analysis and building networks for co-citation, coupling,
scientific collaboration and co-word analysis.

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
