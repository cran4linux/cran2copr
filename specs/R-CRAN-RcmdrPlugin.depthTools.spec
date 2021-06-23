%global __brp_check_rpaths %{nil}
%global packname  RcmdrPlugin.depthTools
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}%{?buildtag}
Summary:          R Commander Depth Tools Plug-in

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    xorg-x11-server-Xvfb
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rcmdr >= 1.4.0
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-depthTools 
Requires:         R-CRAN-Rcmdr >= 1.4.0
Requires:         R-tcltk 
Requires:         R-CRAN-depthTools 

%description
We provide an Rcmdr plug-in based on the depthTools package, which
implements different robust statistical tools for the description and
analysis of gene expression data based on the Modified Band Depth, namely,
the scale curves for visualizing the dispersion of one or various groups
of samples (e.g. types of tumors), a rank test to decide whether two
groups of samples come from a single distribution and two methods of
supervised classification techniques, the DS and TAD methods.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
xvfb-run %{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
