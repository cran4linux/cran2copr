%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TAF
%global packver   4.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Transparent Assessment Framework for Reproducible Research

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-grDevices 
Requires:         R-CRAN-lattice 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
General framework to organize data, methods, and results used in
reproducible scientific analyses. A TAF analysis consists of four scripts
(data.R, model.R, output.R, report.R) that are run sequentially. Each
script starts by reading files from a previous step and ends with writing
out files for the next step. Convenience functions are provided to version
control the required data and software, run analyses, clean residues from
previous runs, manage files, manipulate tables, and produce figures. With
a focus on stability and reproducible analyses, the TAF package comes with
no dependencies. TAF forms a base layer for the 'icesTAF' package and
other scientific applications.

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
