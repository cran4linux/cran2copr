%global __brp_check_rpaths %{nil}
%global packname  metamicrobiomeR
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Microbiome Data Analysis & Meta-Analysis with GAMLSS-BEZI & Random Effects

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gamlss 
BuildRequires:    R-CRAN-meta 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-zCompositions 
BuildRequires:    R-CRAN-compositions 
Requires:         R-CRAN-gamlss 
Requires:         R-CRAN-meta 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-gdata 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-lmerTest 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-zCompositions 
Requires:         R-CRAN-compositions 

%description
Generalized Additive Model for Location, Scale and Shape (GAMLSS) with
zero inflated beta (BEZI) family for analysis of microbiome relative
abundance data (with various options for data transformation/normalization
to address compositional effects) and random effects meta-analysis models
for meta-analysis pooling estimates across microbiome studies are
implemented. Random Forest model to predict microbiome age based on
relative abundances of shared bacterial genera with the Bangladesh data
(Subramanian et al 2014), comparison of multiple diversity indexes using
linear/linear mixed effect models and some data display/visualization are
also implemented. The reference paper is published by Ho NT, Li F, Wang S,
Kuhn L (2019) <doi:10.1186/s12859-019-2744-2> .

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
