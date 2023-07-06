%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  StratigrapheR
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Integrated Stratigraphy

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-diagram 
BuildRequires:    R-CRAN-reshape 
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-XML 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-diagram 
Requires:         R-CRAN-reshape 

%description
Includes bases for litholog generation: graphical functions based on R
base graphics, interval management functions and svg importation functions
among others. Also include stereographic projection functions, and other
functions made to deal with large datasets while keeping options to get
into the details of the data. When using for publication please cite
Sebastien Wouters, Anne-Christine Da Silva, Frederic Boulvain and Xavier
Devleeschouwer, 2021. The R Journal 13:2, 153-178. The palaeomagnetism
functions are based on: Tauxe, L., 2010. Essentials of Paleomagnetism.
University of California Press.
<https://earthref.org/MagIC/books/Tauxe/Essentials/>; Allmendinger, R. W.,
Cardozo, N. C., and Fisher, D., 2013, Structural Geology Algorithms:
Vectors & Tensors: Cambridge, England, Cambridge University Press, 289
pp.; Cardozo, N., and Allmendinger, R. W., 2013, Spherical projections
with OSXStereonet: Computers & Geosciences, v. 51, no. 0, p. 193 - 205,
<doi: 10.1016/j.cageo.2012.07.021>.

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
