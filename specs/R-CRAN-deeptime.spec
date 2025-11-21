%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  deeptime
%global packver   2.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Plotting Tools for Anyone Working in Deep Time

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-deeptimedata 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-ggfittext 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-grImport2 
BuildRequires:    R-CRAN-ggh4x 
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-deeptimedata 
Requires:         R-utils 
Requires:         R-CRAN-ggforce 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-gtable 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-ggfittext 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-grImport2 
Requires:         R-CRAN-ggh4x 

%description
Extends the functionality of other plotting packages (notably 'ggplot2')
to help facilitate the plotting of data over long time intervals,
including, but not limited to, geological, evolutionary, and ecological
data. The primary goal of 'deeptime' is to enable users to add highly
customizable timescales to their visualizations. Other functions are also
included to assist with other areas of deep time visualization.

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
