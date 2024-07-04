%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  neuroimaGene
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Transcriptomic Atlas of Neuroimaging Derived Phenotypes

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-ggseg 
BuildRequires:    R-CRAN-RSQLite 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-ggseg 
Requires:         R-CRAN-RSQLite 

%description
Contains functions to query and visualize the Neuroimaging features
associated with genetically regulated gene expression (GReX). The primary
utility, neuroimaGene(), relies on a list of user-defined genes and
returns a table of neuroimaging features (NIDPs) associated with each
gene. This resource is designed to assist in the interpretation of
genome-wide and transcriptome-wide association studies that evaluate brain
related traits. Bledsoe (2024) <doi:10.1016/j.ajhg.2024.06.002>. In
addition there are several visualization functions that generate summary
plots and 2-dimensional visualizations of regional brain measures.
Mowinckel (2020).

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
