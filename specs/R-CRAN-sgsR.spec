%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sgsR
%global packver   1.4.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.5
Release:          1%{?dist}%{?buildtag}
Summary:          Structurally Guided Sampling

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-clhs 
BuildRequires:    R-CRAN-SamplingBigData 
BuildRequires:    R-CRAN-BalancedSampling 
BuildRequires:    R-CRAN-spatstat.geom 
Requires:         R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-clhs 
Requires:         R-CRAN-SamplingBigData 
Requires:         R-CRAN-BalancedSampling 
Requires:         R-CRAN-spatstat.geom 

%description
Structurally guided sampling (SGS) approaches for airborne laser scanning
(ALS; LIDAR). Primary functions provide means to generate data-driven
stratifications & methods for allocating samples. Intermediate functions
for calculating and extracting important information about input
covariates and samples are also included. Processing outcomes are intended
to help forest and environmental management practitioners better optimize
field sample placement as well as assess and augment existing sample
networks in the context of data distributions and conditions. ALS data is
the primary intended use case, however any rasterized remote sensing data
can be used, enabling data-driven stratifications and sampling approaches.

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
