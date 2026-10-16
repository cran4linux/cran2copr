%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  InterconectaR
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Psychological Network Analysis and Psychometric Insights

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-bootnet 
BuildRequires:    R-CRAN-Cairo 
BuildRequires:    R-CRAN-correlation 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-EGAnet 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-ggplotify 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-mgm 
BuildRequires:    R-CRAN-networktools 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-semPlot 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-wesanderson 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-bootnet 
Requires:         R-CRAN-Cairo 
Requires:         R-CRAN-correlation 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-EGAnet 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-ggplotify 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-mgm 
Requires:         R-CRAN-networktools 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-png 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-qgraph 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-semPlot 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-wesanderson 

%description
Estimates psychological networks by group for research in the social
sciences and complements them with psychometric modeling. It summarises
centrality and bridge centrality indices, evaluates the stability of edges
and centrality from bootstrap results, refines items by the stability of
exploratory graph analysis (EGA), and plots networks with the variance
explained of each node. It also estimates an a priori sample size for EGA
through Monte Carlo simulation and includes an interactive application to
plan the sample size of a network study. Methods follow Epskamp, Borsboom
and Fried (2018) <doi:10.3758/s13428-017-0862-1> and Golino and Epskamp
(2017) <doi:10.1371/journal.pone.0174035>.

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
