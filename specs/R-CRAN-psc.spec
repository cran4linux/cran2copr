%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  psc
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Personalised Synthetic Controls

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-enrichwith 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-flexsurv 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-survminer 
BuildRequires:    R-CRAN-gtsummary 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-waffle 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-enrichwith 
Requires:         R-stats 
Requires:         R-CRAN-flexsurv 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-survminer 
Requires:         R-CRAN-gtsummary 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-waffle 

%description
Allows the comparison of data cohorts (DC) against a Counter Factual Model
(CFM) and measures the difference in terms of an efficacy parameter.
Allows the application of Personalised Synthetic Controls.

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
