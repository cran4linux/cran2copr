%global __brp_check_rpaths %{nil}
%global packname  CytOpT
%global packver   0.9.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.4
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal Transport for Gating Transfer in Cytometry Data with Domain Adaptation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-testthat >= 3.0.0
BuildRequires:    R-CRAN-MetBrewer 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-testthat >= 3.0.0
Requires:         R-CRAN-MetBrewer 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-reticulate 
Requires:         R-stats 

%description
Supervised learning from a source distribution (with known segmentation
into cell sub-populations) to fit a target distribution with unknown
segmentation. It relies regularized optimal transport to directly estimate
the different cell population proportions from a biological sample
characterized with flow cytometry measurements. It is based on the
regularized Wasserstein metric to compare cytometry measurements from
different samples, thus accounting for possible mis-alignment of a given
cell population across sample (due to technical variability from the
technology of measurements). Supervised learning technique based on the
Wasserstein metric that is used to estimate an optimal re-weighting of
class proportions in a mixture model Details are presented in Freulon P,
Bigot J and Hejblum BP (2021) <arXiv:2006.09003>.

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
