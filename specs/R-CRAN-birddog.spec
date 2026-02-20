%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  birddog
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Sniffing Emergence and Trajectories in Academic Papers and Patents

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggraph 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-tidygraph 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-openalexR 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggraph 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-tidygraph 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-openalexR 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-stringr 

%description
Provides a unified set of methods to detect scientific emergence and
technological trajectories in academic papers and patents. The package
combines citation network analysis with community detection and attribute
extraction, also applying natural language processing (NLP) and structural
topic modeling (STM) to uncover the contents of research communities. It
implements metrics and visualizations of community trajectories, including
novelty indicators, citation cycle time, and main path analysis, allowing
researchers to map and interpret the dynamics of emerging knowledge
fields. Applications of the method include: Souza et al. (2022)
<doi:10.1002/bbb.2441>, Souza et al. (2022) <doi:10.14211/ibjesb.e1742>,
Matos et al. (2023) <doi:10.1007/s43938-023-00036-3>, Maria et al. (2023)
<doi:10.3390/su15020967>, Biazatti et al. (2024)
<doi:10.1016/j.envdev.2024.101074>, Felizardo et al. (2025)
<doi:10.1007/s12649-025-03136-z>, and Miranda et al. (2025)
<doi:10.1016/j.ijhydene.2025.01.089>.

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
