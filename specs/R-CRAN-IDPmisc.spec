%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  IDPmisc
%global packver   1.1.21
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.21
Release:          1%{?dist}%{?buildtag}
Summary:          'Utilities of Institute of Data Analyses and Process Design (www.zhaw.ch/idp)'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-methods 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-lattice 
Requires:         R-methods 
Requires:         R-grid 
Requires:         R-CRAN-lattice 

%description
Different high-level graphics functions for displaying large datasets,
displaying circular data in a very flexible way, finding local maxima,
brewing color ramps, drawing nice arrows, zooming 2D-plots, creating
figures with differently colored margin and plot region.  In addition, the
package contains auxiliary functions for data manipulation like omitting
observations with irregular values or selecting data by logical vectors,
which include NAs. Other functions are especially useful in spectroscopy
and analyses of environmental data: robust baseline fitting, finding peaks
in spectra, converting humidity measures.

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
