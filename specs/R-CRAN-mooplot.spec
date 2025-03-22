%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mooplot
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Graphical Visualizations for Multi-Objective Optimization

License:          LGPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-collapse >= 2.0.8
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-moocore 
Requires:         R-CRAN-collapse >= 2.0.8
Requires:         R-CRAN-Rdpack 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-moocore 

%description
Visualization of multi-dimensional data arising in multi-objective
optimization, including plots of the empirical attainment function (EAF),
M. López-Ibáñez, L. Paquete, and T. Stützle (2010)
<doi:10.1007/978-3-642-02538-9_9>, and symmetric Vorob'ev expectation and
deviation, M. Binois, D. Ginsbourger, O. Roustant (2015)
<doi:10.1016/j.ejor.2014.07.032>, among others.

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
