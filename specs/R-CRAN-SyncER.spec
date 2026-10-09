%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SyncER
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Synchronicity Testing for Event Records

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-pracma 

%description
Evaluation of synchronous deposition across different event records using
a log-ratio approach, and syncing age-depth models based on the
availability of isochrons. Following the methodology of Wils & Ramisch
(2026) <doi:10.1038/s41598-026-67943-7>. The synthetic example dataset
used in the examples, tests and vignette is distributed separately in the
companion data package 'SyncERdata'.

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
