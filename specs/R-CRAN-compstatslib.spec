%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  compstatslib
%global packver   0.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive 2D and 3D Visualization of Data and Statistical Concepts

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-miniUI 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-miniUI 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-shiny 

%description
Interactive gadgets and plotting functions for visualizing data sets and
statistical concepts in two and three dimensions. Explore a data frame as
a 3D point cloud you can rotate, fit a moderated (interaction) regression
and view its surface as a 3D wireframe, or plot principal components and
regression fits in two dimensions. Each interactive gadget returns the
call that reproduces its final view, including the viewing angle, so an
exploratory session can be pasted into a script or report. Also provides
simulation-based demonstrations of sampling distributions, confidence
intervals, t-tests, and matrix inversion for teaching and self-study.

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
