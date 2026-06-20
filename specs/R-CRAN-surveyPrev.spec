%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  surveyPrev
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Mapping the Prevalence of Binary Indicators using Survey Data in Small Areas

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rdhs 
BuildRequires:    R-CRAN-SUMMER 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-expss 
BuildRequires:    R-CRAN-labelled 
BuildRequires:    R-CRAN-sjlabelled 
BuildRequires:    R-CRAN-naniar 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-survey 
Requires:         R-stats 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rdhs 
Requires:         R-CRAN-SUMMER 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggridges 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-expss 
Requires:         R-CRAN-labelled 
Requires:         R-CRAN-sjlabelled 
Requires:         R-CRAN-naniar 
Requires:         R-CRAN-jsonlite 

%description
Provides a pipeline to perform small area estimation and prevalence
mapping of binary indicators using health and demographic survey data,
described in Dong et al. (2026) <doi:10.1093/jssam/smaf048>, Wakefield et
al. (2025) <doi:10.48550/arXiv.2110.09576> and Wakefield et al. (2020)
<doi:10.1111/insr.12400>.

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
