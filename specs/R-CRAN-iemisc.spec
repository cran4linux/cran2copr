%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  iemisc
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Irucka Embry's Miscellaneous Functions

License:          GPL (>= 3) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-CHNOSZ >= 1.3.3
BuildRequires:    R-CRAN-rivr >= 1.2.2
BuildRequires:    R-CRAN-data.table >= 1.10.2
BuildRequires:    R-CRAN-USA.state.boundaries >= 1.0.1
BuildRequires:    R-CRAN-units >= 0.7.0
BuildRequires:    R-CRAN-gsubfn >= 0.7
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-iemiscdata 
BuildRequires:    R-CRAN-fpCompare 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-qdapTools 
BuildRequires:    R-CRAN-ramify 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-measurements 
BuildRequires:    R-CRAN-roperators 
BuildRequires:    R-CRAN-berryFunctions 
BuildRequires:    R-CRAN-round 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-matlab 
BuildRequires:    R-CRAN-sjmisc 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-anytime 
BuildRequires:    R-CRAN-qdapRegex 
BuildRequires:    R-CRAN-mgsub 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-matlab2r 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-CRAN-CHNOSZ >= 1.3.3
Requires:         R-CRAN-rivr >= 1.2.2
Requires:         R-CRAN-data.table >= 1.10.2
Requires:         R-CRAN-USA.state.boundaries >= 1.0.1
Requires:         R-CRAN-units >= 0.7.0
Requires:         R-CRAN-gsubfn >= 0.7
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-iemiscdata 
Requires:         R-CRAN-fpCompare 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-qdapTools 
Requires:         R-CRAN-ramify 
Requires:         R-CRAN-foreach 
Requires:         R-stats 
Requires:         R-CRAN-measurements 
Requires:         R-CRAN-roperators 
Requires:         R-CRAN-berryFunctions 
Requires:         R-CRAN-round 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-matlab 
Requires:         R-CRAN-sjmisc 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-anytime 
Requires:         R-CRAN-qdapRegex 
Requires:         R-CRAN-mgsub 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-matlab2r 
Requires:         R-CRAN-signal 
Requires:         R-utils 
Requires:         R-methods 

%description
A collection of Irucka Embry's miscellaneous functions (Engineering
Economics, Civil & Environmental/Water Resources Engineering, Construction
Measurements, GNU Octave compatible functions, Python compatible function,
Trigonometric functions in degrees and function in radians, Geometry,
Statistics, Mortality Calculators, Quick Search, etc.).

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
