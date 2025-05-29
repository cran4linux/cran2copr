%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OmicNavigator
%global packver   1.15.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.15.0
Release:          1%{?dist}%{?buildtag}
Summary:          Open-Source Software for 'Omic' Data Analysis and Visualization

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.12.4
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-data.table >= 1.12.4
Requires:         R-graphics 
Requires:         R-CRAN-jsonlite 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
A tool for interactive exploration of the results from 'omics' experiments
to facilitate novel discoveries from high-throughput biology. The software
includes R functions for the 'bioinformatician' to deposit study metadata
and the outputs from statistical analyses (e.g. differential expression,
enrichment). These results are then exported to an interactive JavaScript
dashboard that can be interrogated on the user's local machine or deployed
online to be explored by collaborators. The dashboard includes 'sortable'
tables, interactive plots including network visualization, and
fine-grained filtering based on statistical significance.

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
