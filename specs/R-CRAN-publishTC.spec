%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  publishTC
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Tools to Help to Publish the Trend-Cycle Component

License:          EUPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rjd3x13 >= 3.3.0
BuildRequires:    R-CRAN-rjd3filters >= 2.4.0
BuildRequires:    R-CRAN-rjd3jars >= 0.0.5
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-rjd3x13 >= 3.3.0
Requires:         R-CRAN-rjd3filters >= 2.4.0
Requires:         R-CRAN-rjd3jars >= 0.0.5
Requires:         R-CRAN-rJava 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-zoo 

%description
Tools to facilitate the computation of the trend-cycle component of time
series. In particular, the computation can be performed using: the Cascade
Linear Filter ('CLF', Dagum and Luati, 2008), classical Henderson
symmetric filters with surrogate Musgrave asymmetric filters, local
parameterizations of Musgrave filters (Quartier-la-Tente, 2024), and
robust extensions taking into account additive outliers and level shifts
(Quartier-la-Tente, 2025). Computes confidence intervals and provides
specialized plotting functions for publication.

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
