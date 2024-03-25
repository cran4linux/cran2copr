%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggtern
%global packver   3.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          An Extension to 'ggplot2', for the Creation of Ternary Diagrams

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-compositions >= 2.0.2
BuildRequires:    R-CRAN-plyr >= 1.8.3
BuildRequires:    R-CRAN-scales >= 1.3.0
BuildRequires:    R-CRAN-hexbin >= 1.28.2
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-proto >= 1.0
BuildRequires:    R-CRAN-latex2exp >= 0.5
BuildRequires:    R-CRAN-gtable >= 0.1.2
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-methods 
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-compositions >= 2.0.2
Requires:         R-CRAN-plyr >= 1.8.3
Requires:         R-CRAN-scales >= 1.3.0
Requires:         R-CRAN-hexbin >= 1.28.2
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-proto >= 1.0
Requires:         R-CRAN-latex2exp >= 0.5
Requires:         R-CRAN-gtable >= 0.1.2
Requires:         R-grid 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-lattice 
Requires:         R-methods 

%description
Extends the functionality of 'ggplot2', providing the capability to plot
ternary diagrams for (subset of) the 'ggplot2' geometries. Additionally,
'ggtern' has implemented several NEW geometries which are unavailable to
the standard 'ggplot2' release. For further examples and documentation,
please proceed to the 'ggtern' website.

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
