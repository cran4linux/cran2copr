%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mortar
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Standardize Data Science Workflows

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-gert 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-usethis 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-gert 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-usethis 

%description
Helper functions to standardizes common workflows in the USGS Data Science
Community of Practice to produce more robust, reproducible pipelines. It
contains helper functions to standardize (1) the organization of project
repositories and (2) the creation ofpipelines from the 'targets' R Package
(Landau et al. (2026) <doi:10.5281/zenodo.18555866>), using the DS CoP
best practices. We draw upon community developed best practices as well as
certain USGS-specific requirements. See Shrycock et al. (2023)
<doi:10.3133/tm7B2> for examples of these USGS requirements.

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
