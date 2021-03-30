%global packname  glycanr
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Analysing N-Glycan Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 0.4.3
BuildRequires:    R-CRAN-tidyr >= 0.3.1
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-coin 
Requires:         R-CRAN-dplyr >= 0.4.3
Requires:         R-CRAN-tidyr >= 0.3.1
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-coin 

%description
Useful utilities in N-glycan data analysis. This package tries to fill the
gap in N-glycan data analysis by providing easy to use functions for basic
operations on data (see <https://en.wikipedia.org/wiki/Glycomics> for more
details on Glycomics). At the moment 'glycanr' is mostly oriented to data
obtained by UPLC (Ultra Performance Liquid Chromatography) and LCMS
(Liquid chromatography–mass spectrometry) analysis of Plasma and IgG
glycome.

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
