%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AnimalSequences
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analyse Animal Sequential Behaviour and Communication

License:          Apache License (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidytext 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-fpc 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-apcluster 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-ggraph 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-naivebayes 
BuildRequires:    R-CRAN-ranger 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidytext 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-fpc 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-apcluster 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tibble 
Requires:         R-stats 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-ggraph 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-naivebayes 
Requires:         R-CRAN-ranger 

%description
All animal behaviour occurs sequentially. The package has a number of
functions to format sequence data from different sources, to analyse
sequential behaviour and communication in animals. It also has functions
to plot the data and to calculate the entropy of sequences.

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
