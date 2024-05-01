%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  petersenlab
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Collection of R Functions by the Petersen Lab

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-mitools 
BuildRequires:    R-CRAN-mix 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-scales 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-mitools 
Requires:         R-CRAN-mix 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-xtable 
Requires:         R-grDevices 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-viridisLite 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-scales 

%description
A collection of R functions that are widely used by the Petersen Lab.
Included are functions for various purposes, including evaluating the
accuracy of judgments and predictions, performing scoring of assessments,
generating correlation matrices, conversion of data between various types,
data management, psychometric evaluation, extensions related to latent
variable modeling, various plotting capabilities, and other miscellaneous
useful functions. By making the package available, we hope to make our
methods reproducible and replicable by others and to help others perform
their data processing and analysis methods more easily and efficiently.
The codebase is in <doi:10.5281/zenodo.7602890>. The package is described
in Petersen (2024) <doi:10.1201/9781003357421>,
<doi:10.5281/zenodo.6466590>.

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
