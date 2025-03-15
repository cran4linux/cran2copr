%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  trace
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tandem Repeat Analysis by Capillary Electrophoresis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-seqinr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-lme4 
Requires:         R-methods 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-seqinr 
Requires:         R-CRAN-shiny 
Requires:         R-stats 
Requires:         R-utils 

%description
A pipeline for short tandem repeat instability analysis from fragment
analysis data. Inputs of fsa files or peak tables, and a user supplied
metadata data-frame. The package identifies ladders, calls peaks,
identifies the modal peaks, calls repeats, then calculates repeat
instability metrics (e.g. expansion index from Lee et al. (2010)
<doi:10.1186/1752-0509-4-29>).

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
