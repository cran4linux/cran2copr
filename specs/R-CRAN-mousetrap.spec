%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mousetrap
%global packver   3.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Process and Analyze Mouse-Tracking Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-psych >= 1.2.4
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.4
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-diptest 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-cstab 
BuildRequires:    R-CRAN-fastcluster 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-psych >= 1.2.4
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-Rcpp >= 0.11.4
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-magrittr 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-diptest 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-cstab 
Requires:         R-CRAN-fastcluster 
Requires:         R-parallel 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-lifecycle 

%description
Mouse-tracking, the analysis of mouse movements in computerized
experiments, is a method that is becoming increasingly popular in the
cognitive sciences. The mousetrap package offers functions for importing,
preprocessing, analyzing, aggregating, and visualizing mouse-tracking
data. An introduction into mouse-tracking analyses using mousetrap can be
found in Wulff, Kieslich, Henninger, Haslbeck, & Schulte-Mecklenbeck
(2023) <doi:10.31234/osf.io/v685r> (preprint:
<https://osf.io/preprints/psyarxiv/v685r>).

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
