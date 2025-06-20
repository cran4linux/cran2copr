%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  diceR
%global packver   3.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Diverse Cluster Ensemble in R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildRequires:    R-CRAN-dplyr >= 0.7.5
BuildRequires:    R-CRAN-purrr >= 0.2.3
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-class 
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-CRAN-clusterCrit 
BuildRequires:    R-CRAN-clValid 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-infotheo 
BuildRequires:    R-CRAN-klaR 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pheatmap 
BuildRequires:    R-CRAN-RankAggreg 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-yardstick 
Requires:         R-CRAN-dplyr >= 0.7.5
Requires:         R-CRAN-purrr >= 0.2.3
Requires:         R-CRAN-abind 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-class 
Requires:         R-CRAN-clue 
Requires:         R-CRAN-clusterCrit 
Requires:         R-CRAN-clValid 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-CRAN-infotheo 
Requires:         R-CRAN-klaR 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-mclust 
Requires:         R-methods 
Requires:         R-CRAN-pheatmap 
Requires:         R-CRAN-RankAggreg 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-yardstick 

%description
Performs cluster analysis using an ensemble clustering framework, Chiu &
Talhouk (2018) <doi:10.1186/s12859-017-1996-y>. Results from a diverse set
of algorithms are pooled together using methods such as majority voting,
K-Modes, LinkCluE, and CSPA. There are options to compare cluster
assignments across algorithms using internal and external indices,
visualizations such as heatmaps, and significance testing for the
existence of clusters.

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
