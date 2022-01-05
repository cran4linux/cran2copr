%global __brp_check_rpaths %{nil}
%global packname  RcmdrPlugin.NMBU
%global packver   1.8.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.13
Release:          1%{?dist}%{?buildtag}
Summary:          R Commander Plug-in for University Level Applied Statistics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    xorg-x11-server-Xvfb
BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rcmdr >= 2.1.7
BuildRequires:    R-CRAN-mixlm >= 1.2.3
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-phia 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-car 
Requires:         R-CRAN-Rcmdr >= 2.1.7
Requires:         R-CRAN-mixlm >= 1.2.3
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-phia 
Requires:         R-tcltk 
Requires:         R-CRAN-car 

%description
An R Commander "plug-in" extending functionality of linear models and
providing an interface to Partial Least Squares Regression and Linear and
Quadratic Discriminant analysis. Several statistical summaries are
extended, predictions are offered for additional types of analyses, and
extra plots, tests and mixed models are available.

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
xvfb-run %{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
