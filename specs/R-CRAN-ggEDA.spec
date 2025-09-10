%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggEDA
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Turnkey Visualisations for Exploratory Data Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-patchwork >= 1.3.0
BuildRequires:    R-CRAN-ggiraph >= 0.8.11
BuildRequires:    R-CRAN-assertions >= 0.2.0
BuildRequires:    R-CRAN-rank >= 0.1.1
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggtext 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-patchwork >= 1.3.0
Requires:         R-CRAN-ggiraph >= 0.8.11
Requires:         R-CRAN-assertions >= 0.2.0
Requires:         R-CRAN-rank >= 0.1.1
Requires:         R-CRAN-cli 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggtext 
Requires:         R-grDevices 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 

%description
Provides interactive visualisations for exploratory data analysis of
high-dimensional datasets. Includes parallel coordinate plots for
exploring large datasets with mostly quantitative features, but also
stacked one-dimensional visualisations that more effectively show
missingness and complex categorical relationships in smaller datasets.

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
