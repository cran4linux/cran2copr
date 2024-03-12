%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LipinskiFilters
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Computes and Visualize Lipinski's Parameters

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rcdk >= 3.8.1
BuildRequires:    R-CRAN-itertools >= 0.1.3
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-rcdk >= 3.8.1
Requires:         R-CRAN-itertools >= 0.1.3
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-ggplot2 
Requires:         R-utils 
Requires:         R-CRAN-knitr 

%description
This computes Lipinski Rule of Five parameters and offers visualization
for drug discovery. It analyzes molecular properties like molecular
weight, hydrogen bond donors, acceptors, and ALogP, providing histograms
and pass/fail status plots for efficient compound evaluation, aiding in
drug development.

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
