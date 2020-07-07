%global packname  asbio
%global packver   1.6-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.5
Release:          2%{?dist}
Summary:          A Collection of Statistical Tools for Biologists

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    xorg-x11-server-Xvfb
Requires:         bwidget
BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildArch:        noarch
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-CRAN-pixmap 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-tkrplot 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-multcompView 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-gWidgets2 
BuildRequires:    R-CRAN-gWidgets2tcltk 
Requires:         R-tcltk 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-CRAN-pixmap 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-deSolve 
Requires:         R-lattice 
Requires:         R-CRAN-tkrplot 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-multcompView 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-gWidgets2 
Requires:         R-CRAN-gWidgets2tcltk 

%description
Contains functions from: Aho, K. (2014) Foundational and Applied
Statistics for Biologists using R.  CRC/Taylor and Francis, Boca Raton,
FL, ISBN: 978-1-4398-7338-0.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
xvfb-run %{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
