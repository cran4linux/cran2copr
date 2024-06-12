%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qlcVisualize
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Visualization for Quantitative Language Comparison

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-qlcMatrix 
BuildRequires:    R-CRAN-seriation 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-spatstat.random 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-mapplots 
BuildRequires:    R-CRAN-geodata 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-alphahull 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-concaveman 
BuildRequires:    R-CRAN-cartogramR 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-qlcMatrix 
Requires:         R-CRAN-seriation 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-spatstat.random 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-mapplots 
Requires:         R-CRAN-geodata 
Requires:         R-methods 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-alphahull 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-concaveman 
Requires:         R-CRAN-cartogramR 

%description
Collection of visualizations as used in quantitative language comparison.
Currently implemented are visualisations dealing nominal data with
multiple levels ("level map" and "factor map"), and assistance for making
weighted geographical Voronoi-maps ("weighted map").

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
