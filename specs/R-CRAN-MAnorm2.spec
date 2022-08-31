%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MAnorm2
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Normalizing and Comparing ChIP-seq Samples

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-locfit >= 1.5.9
BuildRequires:    R-CRAN-statmod >= 1.4.34
BuildRequires:    R-CRAN-scales >= 0.3.0
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
Requires:         R-CRAN-locfit >= 1.5.9
Requires:         R-CRAN-statmod >= 1.4.34
Requires:         R-CRAN-scales >= 0.3.0
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-methods 

%description
Chromatin immunoprecipitation followed by high-throughput sequencing
(ChIP-seq) is the premier technology for profiling genome-wide
localization of chromatin-binding proteins, including transcription
factors and histones with various modifications. This package provides a
robust method for normalizing ChIP-seq signals across individual samples
or groups of samples. It also designs a self-contained system of
statistical models for calling differential ChIP-seq signals between two
or more biological conditions as well as for calling hypervariable
ChIP-seq signals across samples. Refer to Tu et al. (2021)
<doi:10.1101/gr.262675.120> and Chen et al. (2022)
<doi:10.1186/s13059-022-02627-9> for associated statistical details.

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
