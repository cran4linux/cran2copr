%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CICA
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Clusterwise Independent Component Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3
Requires:         R-core >= 4.3
BuildArch:        noarch
BuildRequires:    R-CRAN-ica 
BuildRequires:    R-CRAN-RNifti 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-multiway 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-neurobase 
BuildRequires:    R-CRAN-oro.nifti 
BuildRequires:    R-CRAN-servr 
BuildRequires:    R-CRAN-htmltools 
Requires:         R-CRAN-ica 
Requires:         R-CRAN-RNifti 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-multiway 
Requires:         R-methods 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-neurobase 
Requires:         R-CRAN-oro.nifti 
Requires:         R-CRAN-servr 
Requires:         R-CRAN-htmltools 

%description
Clustering multi-subject resting state functional Magnetic Resonance
Imaging data. This methods enables the clustering of subjects based on
multi-subject resting state functional Magnetic Resonance Imaging data.
Objects are clustered based on similarities and differences in
cluster-specific estimated components obtained by Independent Component
Analysis.

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
