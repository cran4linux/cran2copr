%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HawaSpatial
%global packver   0.1.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.10
Release:          1%{?dist}%{?buildtag}
Summary:          Holistic and Areal Weighted Analysis for Global Development

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-shiny 

%description
Provides a 'shiny'-based platform for sub-national monitoring of global
development indicators using large-scale household surveys. The package
supports the Demographic and Health Surveys, Multiple Indicator Cluster
Surveys, Malaria Indicator Surveys, Integrated Household Budget Surveys,
Service Provision Assessment surveys, and Living Standards Measurement
Study surveys. It provides workflows for descriptive, diagnostic,
predictive, and prescriptive spatial analytics, including a spatial
equalizer for survey-shapefile integration, exploratory spatial data
analysis, area-level small area estimation, spatial autoregressive and
spatial error models, hierarchical multilevel models, spatial inequality
metrics, spatial and temporal decomposition, and publication-ready
reporting. The implemented methods are described in
<doi:10.1111/j.1538-4632.1995.tb00338.x>, <doi:10.1007/s11749-018-0599-x>,
and the reference identified by <isbn:9781118735787>. The software has
been cited in applied geographic and multilevel health studies, including
studies of arthritis resource allocation <doi:10.1016/j.jorep.2026.101000>
and childhood stunting priorities <doi:10.1016/j.nutos.2026.100660>.

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
