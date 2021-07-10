%global __brp_check_rpaths %{nil}
%global packname  popsom
%global packver   5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.2
Release:          1%{?dist}%{?buildtag}
Summary:          A Very Efficient Implementation of Kohonen's Self-Organizing Maps (SOMs) with Starburst Visualizations

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
Kohonen's self-organizing maps with a number of distinguishing features:
(1) A very efficient, single threaded, stochastic training algorithm based
on ideas from tensor algebra.  Up to 60x faster than traditional
single-threaded training algorithms. No special accelerator hardware
required. (2) Automatic centroid detection and visualization using
starbursts. (3) Two models of the data: (a) a self-organizing map model,
(b) a centroid based clustering model. (4) A number of easily accessible
quality metrics for the self-organizing map and the centroid based cluster
model.

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
