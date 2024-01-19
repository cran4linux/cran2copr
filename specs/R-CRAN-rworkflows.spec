%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rworkflows
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Test, Document, Containerise, and Deploy R Packages

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-here 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-desc 
BuildRequires:    R-CRAN-badger 
BuildRequires:    R-CRAN-renv 
BuildRequires:    R-tools 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-BiocManager 
BuildRequires:    R-CRAN-data.table 
Requires:         R-stats 
Requires:         R-CRAN-here 
Requires:         R-CRAN-yaml 
Requires:         R-utils 
Requires:         R-CRAN-desc 
Requires:         R-CRAN-badger 
Requires:         R-CRAN-renv 
Requires:         R-tools 
Requires:         R-methods 
Requires:         R-CRAN-BiocManager 
Requires:         R-CRAN-data.table 

%description
Reproducibility is essential to the progress of research, yet achieving it
remains elusive even in computational fields. Continuous Integration (CI)
platforms offer a powerful way to launch automated workflows to check and
document code, but often require considerable time, effort, and technical
expertise to setup. We therefore developed the rworkflows suite to make
robust CI workflows easy and freely accessible to all R package
developers. rworkflows consists of 1) a CRAN/Bioconductor-compatible R
package template, 2) an R package to quickly implement a standardised
workflow, and 3) a centrally maintained GitHub Action.

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
