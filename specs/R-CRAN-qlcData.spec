%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qlcData
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Processing Data for Quantitative Language Comparison

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-yaml >= 2.1.11
BuildRequires:    R-CRAN-stringi >= 0.2.5
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-docopt 
BuildRequires:    R-CRAN-data.tree 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-ape 
Requires:         R-CRAN-yaml >= 2.1.11
Requires:         R-CRAN-stringi >= 0.2.5
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-docopt 
Requires:         R-CRAN-data.tree 
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-ape 

%description
Functionality to read, recode, and transcode data as used in quantitative
language comparison, specifically to deal with multilingual orthographic
variation (Moran & Cysouw (2018) <doi:10.5281/zenodo.1296780>) and with
the recoding of nominal data.

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
