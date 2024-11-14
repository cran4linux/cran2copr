%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PepMapViz
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Versatile Toolkit for Peptide Mapping, Visualization, and Comparative Exploration

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-ggh4x 
BuildRequires:    R-CRAN-ggnewscale 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-ggh4x 
Requires:         R-CRAN-ggnewscale 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-rlang 

%description
A versatile R visualization package that empowers researchers with
comprehensive visualization tools for seamlessly mapping peptides to
protein sequences, identifying distinct domains and regions of interest,
accentuating mutations, and highlighting post-translational modifications,
all while enabling comparisons across diverse experimental conditions.
Potential applications of 'PepMapViz' include the visualization of
cross-software mass spectrometry results at the peptide level for specific
protein and domain details in a linearized format and post-translational
modification coverage across different experimental conditions; unraveling
insights into disease mechanisms. It also enables visualization of major
histocompatibility complex-presented peptides in different antibody
regions predicting immunogenicity in antibody drug development.

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
