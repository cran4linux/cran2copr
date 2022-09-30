%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  longsurr
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Longitudinal Surrogate Marker Analysis

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-Rsurrogate 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-here 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-KernSmooth 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-fdapace 
BuildRequires:    R-CRAN-grf 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-refund 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-fda.usc 
Requires:         R-CRAN-stringr 
Requires:         R-splines 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-Rsurrogate 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-here 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-KernSmooth 
Requires:         R-stats 
Requires:         R-CRAN-fdapace 
Requires:         R-CRAN-grf 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-mvnfast 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-refund 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-fda.usc 

%description
Assess the proportion of treatment effect explained by a longitudinal
surrogate marker as described in Agniel D and Parast L (2021)
<doi:10.1111/biom.13310>.

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
