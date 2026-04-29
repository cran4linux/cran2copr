%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggInterval
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Visualizing Interval-Valued Data Using 'ggplot2'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-RSDA 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-prodlim 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-vctrs 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-RSDA 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-prodlim 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-ggthemes 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-vctrs 

%description
Extends 'ggplot2' for visualizing interval-valued data with scatter plots,
histograms, index plots, boxplots, radar plots, PCA displays, and
correlation heatmaps. The package also converts classical data tables into
interval-valued data using clustering algorithms or user-defined
groupings.

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
