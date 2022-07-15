%global __brp_check_rpaths %{nil}
%global packname  heuristicsmineR
%global packver   0.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Discovery of Process Models with the Heuristics Miner

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-DiagrammeR >= 1.0.0
BuildRequires:    R-CRAN-processmapR >= 0.3.1
BuildRequires:    R-CRAN-bupaR 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-petrinetR 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-DiagrammeR >= 1.0.0
Requires:         R-CRAN-processmapR >= 0.3.1
Requires:         R-CRAN-bupaR 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-petrinetR 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggthemes 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-stringr 

%description
Provides the heuristics miner algorithm for process discovery as proposed
by Weijters et al. (2011) <doi:10.1109/CIDM.2011.5949453>. The algorithm
builds a causal net from an event log created with the 'bupaR' package.
Event logs are a set of ordered sequences of events for which 'bupaR'
provides the S3 class eventlog(). The discovered causal nets can be
visualised as 'htmlwidgets' and it is possible to annotate them with the
occurrence frequency or processing and waiting time of process activities.

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
