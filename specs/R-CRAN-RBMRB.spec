%global __brp_check_rpaths %{nil}
%global packname  RBMRB
%global packver   2.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          BMRB Data Access and Visualization

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.5.6
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-data.table >= 1.9.8
BuildRequires:    R-CRAN-httr >= 1.2.1
BuildRequires:    R-CRAN-rjson >= 0.2.15
BuildRequires:    R-stats 
Requires:         R-CRAN-plotly >= 4.5.6
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-data.table >= 1.9.8
Requires:         R-CRAN-httr >= 1.2.1
Requires:         R-CRAN-rjson >= 0.2.15
Requires:         R-stats 

%description
The Biological Magnetic Resonance Data Bank (BMRB,<http:// www.bmrb.io/>)
collects, annotates, archives, and disseminates (worldwide in the public
domain) the important spectral and quantitative data derived from
NMR(Nuclear Magnetic Resonance) spectroscopic investigations of biological
macromolecules and metabolites. This package provides an interface to BMRB
database for easy data access and includes a minimal set of data
visualization functions. Users are encouraged to make their own data
visualizations using BMRB data.

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
