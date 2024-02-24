%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  forceplate
%global packver   1.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Processing Force-Plate Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-signal 
Requires:         R-stats 
Requires:         R-CRAN-stringi 

%description
Process raw force-plate data (txt-files) by segmenting them into trials
and, if needed, calculating (user-defined) descriptive statistics of
variables for user-defined time bins (relative to trigger onsets) for each
trial. When segmenting the data a baseline correction, a filter, and a
data imputation can be applied if needed. Experimental data can also be
processed and combined with the segmented force-plate data. This procedure
is suggested by Johannsen et al. (2023) <doi:10.6084/m9.figshare.22190155>
and some of the options (e.g., choice of low-pass filter) are also
suggested by Winter (2009) <doi:10.1002/9780470549148>.

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
