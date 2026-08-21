%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RIFanalysis
%global packver   0.9.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.2
Release:          1%{?dist}%{?buildtag}
Summary:          Relative Importance Factor Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-poweRlaw >= 0.70.0
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggraph 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-poweRlaw >= 0.70.0
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggraph 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-stringr 

%description
Tools for estimating, comparing, and visualizing Relative Importance
Factor (RIF) indices based on rank-frequency distributions and discrete
power-law models. The package provides reproducible workflows for data
preparation, model fitting, goodness-of-fit assessment, bootstrap
inference, and publication-ready outputs. The implemented methodology is
described in Llinas et al. (2026) <doi:10.3390/math14060966>.

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
