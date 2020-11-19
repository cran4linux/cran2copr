%global packname  latrend
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Framework for Clustering Longitudinal Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-caret >= 6.0
BuildRequires:    R-CRAN-mclust >= 5.4.5
BuildRequires:    R-stats >= 3.6.0
BuildRequires:    R-methods >= 3.6.0
BuildRequires:    R-CRAN-R.utils >= 2.9.0
BuildRequires:    R-CRAN-longitudinalData >= 2.4.1
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-foreach >= 1.4.7
BuildRequires:    R-CRAN-clusterCrit >= 1.2.8
BuildRequires:    R-CRAN-data.table >= 1.12.0
BuildRequires:    R-CRAN-lme4 >= 1.1
BuildRequires:    R-CRAN-scales >= 1.0.0
BuildRequires:    R-CRAN-matrixStats >= 0.55.0
BuildRequires:    R-CRAN-mclustcomp >= 0.3.1
BuildRequires:    R-CRAN-stackoverflow >= 0.3.0
BuildRequires:    R-CRAN-assertthat >= 0.2.1
Requires:         R-CRAN-caret >= 6.0
Requires:         R-CRAN-mclust >= 5.4.5
Requires:         R-stats >= 3.6.0
Requires:         R-methods >= 3.6.0
Requires:         R-CRAN-R.utils >= 2.9.0
Requires:         R-CRAN-longitudinalData >= 2.4.1
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-foreach >= 1.4.7
Requires:         R-CRAN-clusterCrit >= 1.2.8
Requires:         R-CRAN-data.table >= 1.12.0
Requires:         R-CRAN-lme4 >= 1.1
Requires:         R-CRAN-scales >= 1.0.0
Requires:         R-CRAN-matrixStats >= 0.55.0
Requires:         R-CRAN-mclustcomp >= 0.3.1
Requires:         R-CRAN-stackoverflow >= 0.3.0
Requires:         R-CRAN-assertthat >= 0.2.1

%description
A framework for clustering longitudinal datasets in a standardized way.
Provides an interface to existing R packages for clustering longitudinal
univariate trajectories, facilitating reproducible and transparent
analyses. Additionally, standard tools are provided to support cluster
analyses, including repeated estimation, model validation, and model
assessment. The interface enables users to compare results between
methods, and to implement and evaluate new methods with ease.

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
