%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BIOdry
%global packver   0.9.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.5
Release:          1%{?dist}%{?buildtag}
Summary:          Multilevel Modeling of Dendroclimatical Fluctuations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-ecodist 
BuildRequires:    R-CRAN-lattice 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-ecodist 
Requires:         R-CRAN-lattice 

%description
Processes multilevel ecological data series (MEDS) arranged in temporal or
spatial hierarchies defined by sampling designs. The package recursively
applies one-level stage functions to long-format tree-ring and climate
data, then optionally fits a terminal model to the processed series.
Terminal fits currently include mixed-effects detrending through 'nlme'
and Friedman supersmoother detrending through supsmu() of 'stats'. The
package also supports post-detrending comparison and inference tools for
multilevel dendroclimatic analyses. The method is described in Lara et al.
(2018) <doi:10.1371/journal.pone.0196923>.

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
