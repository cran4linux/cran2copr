%global packname  popsom
%global packver   5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Building, Visualizing, and Evaluating Self-Organizing Maps

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-hash 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-fields 
Requires:         R-graphics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-hash 
Requires:         R-stats 
Requires:         R-grDevices 

%description
A self-organizing map package with three distinguishing features: (1)
Automatic cluster centroid detection and visualization using starbursts.
(2) Maintains two models of the data: (a) a self-organizing map model (b)
a centroid based clustering model. (3) A very efficient stochastic
training algorithm based on ideas from tensor algebra.

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
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
