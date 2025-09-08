%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EZFragility
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Compute Neural Fragility for Ictal iEEG Time Series

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-Epoch 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-ggtext 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-ramify 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-Epoch 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-ggtext 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-ramify 
Requires:         R-CRAN-reshape2 

%description
Provides tools to compute the neural fragility matrix from intracranial
electrocorticographic (iEEG) recordings, enabling the analysis of brain
dynamics during seizures. The package implements the method described by
Li et al. (2017) <doi:10.23919/ACC.2017.7963378> and includes functions
for data preprocessing ('Epoch'), fragility computation ('calcAdjFrag'),
and visualization.

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
