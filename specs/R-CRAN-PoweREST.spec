%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PoweREST
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Bootstrap-Based Power Estimation Tool for Spatial Transcriptomics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-scam 
BuildRequires:    R-CRAN-Seurat 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-resample 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rayshader 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-scam 
Requires:         R-CRAN-Seurat 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-resample 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rayshader 
Requires:         R-CRAN-ggplot2 

%description
Power estimation and sample size calculation for 10X Visium Spatial
Transcriptomics data to detect differential expressed genes between two
conditions based on bootstrap resampling. See Shui et al. (2025)
<doi:10.1371/journal.pcbi.1013293> for method details.

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
