%global __brp_check_rpaths %{nil}
%global packname  rplotengine
%global packver   1.0-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.8
Release:          1%{?dist}%{?buildtag}
Summary:          R as a Plotting Engine

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.6.2
Requires:         R-core >= 2.6.2
BuildArch:        noarch
BuildRequires:    R-CRAN-xtable 
Requires:         R-CRAN-xtable 

%description
Generate basic charts either by custom applications, or from a small
script launched from the system console, or within the R console. Two
ASCII text files are necessary: (1) The graph parameters file, which name
is passed to the function 'rplotengine()'. The user can specify the
titles, choose the type of the graph, graph output formats (e.g. png,
eps), proportion of the X-axis and Y-axis, position of the legend, whether
to show or not a grid at the background, etc. (2) The data to be plotted,
which name is specified as a parameter ('data_filename') in the previous
file. This data file has a tabulated format, with a single character (e.g.
tab) between each column. Optionally, the file could include data columns
for showing confidence intervals.

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
