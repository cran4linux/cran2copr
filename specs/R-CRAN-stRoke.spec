%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stRoke
%global packver   23.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          23.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Clinical Stroke Research

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gtsummary 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-rankinPlot 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gtsummary 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-rankinPlot 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 

%description
This is an R-toolbox of custom functions for convenient data management
and analysis in clinical health research and teaching. The package is
mainly collected for personal use, but any use beyond that is encouraged.
This package has migrated functions from 'agdamsbo/daDoctoR', and new
functions has been added. Version follows months and year. See
NEWS/Changelog for release notes. This package includes sampled data from
the TALOS trial (Kraglund et al (2018)
<doi:10.1161/STROKEAHA.117.020067>). The win_prob() function is based on
work by Zou et al (2022) <doi:10.1161/STROKEAHA.121.037744>. The
age_calc() function is based on work by Becker (2020)
<doi:10.18637/jss.v093.i02>.

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
