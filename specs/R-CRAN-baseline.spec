%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  baseline
%global packver   1.3-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.7
Release:          1%{?dist}%{?buildtag}
Summary:          Baseline Correction of Spectra

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-SparseM 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-graphics 
Requires:         R-CRAN-SparseM 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-methods 

%description
Collection of baseline correction algorithms, along with a framework and a
Tcl/Tk enabled GUI for optimising baseline algorithm parameters. Typical
use of the package is for removing background effects from spectra
originating from various types of spectroscopy and spectrometry, possibly
optimizing this with regard to regression or classification results.
Correction methods include polynomial fitting, weighted local smoothers
and many more.

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
