%global __brp_check_rpaths %{nil}
%global packname  PointedSDMs
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Fit Models Derived from Point Processes to Species Distributions using 'inlabru'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-inlabru >= 2.5
BuildRequires:    R-CRAN-sp >= 1.4.5
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-R.devices 
BuildRequires:    R-CRAN-blockCV 
Requires:         R-CRAN-inlabru >= 2.5
Requires:         R-CRAN-sp >= 1.4.5
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-R.devices 
Requires:         R-CRAN-blockCV 

%description
Integrated species distribution modeling is a rising field in quantitative
ecology thanks to significant rises in the quantity of data available,
increases in computational speed and the proven benefits of using such
models. Despite this, the general software to help ecologists construct
such models in an easy-to-use framework is lacking. We therefore introduce
the R package 'PointedSDMs': which provides the tools to help ecologists
set up integrated models and perform inference on them. There are also
functions within the package to help run spatial cross-validation for
model selection, as well as generic plotting and predicting functions. An
introduction to these methods is discussed in Issac, Jarzyna, Keil,
Dambly, Boersch-Supan, Browning, Freeman, Golding, Guillera-Arroita,
Henrys, Jarvis, Lahoz-Monfort, Pagel, Pescott, Schmucki, Simmonds and
O’Hara (2020) <doi:10.1016/j.tree.2019.08.006>.

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
