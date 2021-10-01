%global __brp_check_rpaths %{nil}
%global packname  aplpack
%global packver   1.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.5
Release:          1%{?dist}%{?buildtag}
Summary:          Another Plot Package: 'Bagplots', 'Iconplots', 'Summaryplots', Slider Functions and Others

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch

%description
Some functions for drawing some special plots: The function 'bagplot'
plots a bagplot, 'faces' plots chernoff faces, 'iconplot' plots a
representation of a frequency table or a data matrix, 'plothulls' plots
hulls of a bivariate data set, 'plotsummary' plots a graphical summary of
a data set, 'puticon' adds icons to a plot, 'skyline.hist' combines
several histograms of a one dimensional data set in one plot, 'slider'
functions supports some interactive graphics, 'spin3R' helps an inspection
of a 3-dim point cloud, 'stem.leaf' plots a stem and leaf plot,
'stem.leaf.backback' plots back-to-back versions of stem and leaf plot.

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
