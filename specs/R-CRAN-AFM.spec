%global __brp_check_rpaths %{nil}
%global packname  AFM
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Atomic Force Microscope Image Analysis

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-grid >= 3.1.3
BuildRequires:    R-methods >= 3.1.3
BuildRequires:    R-CRAN-gridExtra >= 2.0
BuildRequires:    R-CRAN-data.table >= 1.9.6
BuildRequires:    R-CRAN-pracma >= 1.8.6
BuildRequires:    R-CRAN-plyr >= 1.8.3
BuildRequires:    R-CRAN-sp >= 1.2.0
BuildRequires:    R-CRAN-mixtools >= 1.0.4
BuildRequires:    R-CRAN-gstat >= 1.0.26
BuildRequires:    R-CRAN-ggplot2 >= 1.0.1
BuildRequires:    R-CRAN-igraph >= 1.0.1
BuildRequires:    R-CRAN-stringr >= 1.0.0
BuildRequires:    R-CRAN-rgl >= 0.96
BuildRequires:    R-CRAN-dbscan >= 0.9.8
BuildRequires:    R-CRAN-fftwtools >= 0.9.8
BuildRequires:    R-CRAN-fractaldim >= 0.8.4
BuildRequires:    R-CRAN-shinyjs >= 0.4.0
BuildRequires:    R-CRAN-scales >= 0.4.0
BuildRequires:    R-CRAN-moments >= 0.14
BuildRequires:    R-CRAN-shiny >= 0.12.2
BuildRequires:    R-CRAN-png >= 0.1.7
Requires:         R-grid >= 3.1.3
Requires:         R-methods >= 3.1.3
Requires:         R-CRAN-gridExtra >= 2.0
Requires:         R-CRAN-data.table >= 1.9.6
Requires:         R-CRAN-pracma >= 1.8.6
Requires:         R-CRAN-plyr >= 1.8.3
Requires:         R-CRAN-sp >= 1.2.0
Requires:         R-CRAN-mixtools >= 1.0.4
Requires:         R-CRAN-gstat >= 1.0.26
Requires:         R-CRAN-ggplot2 >= 1.0.1
Requires:         R-CRAN-igraph >= 1.0.1
Requires:         R-CRAN-stringr >= 1.0.0
Requires:         R-CRAN-rgl >= 0.96
Requires:         R-CRAN-dbscan >= 0.9.8
Requires:         R-CRAN-fftwtools >= 0.9.8
Requires:         R-CRAN-fractaldim >= 0.8.4
Requires:         R-CRAN-shinyjs >= 0.4.0
Requires:         R-CRAN-scales >= 0.4.0
Requires:         R-CRAN-moments >= 0.14
Requires:         R-CRAN-shiny >= 0.12.2
Requires:         R-CRAN-png >= 0.1.7

%description
Provides Atomic Force Microscope images analysis such as Gaussian mixes
identification, Power Spectral Density, roughness against lengthscale,
experimental variogram and variogram models, fractal dimension and scale,
2D network analysis. The AFM images can be exported to STL format for 3D
printing.

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
