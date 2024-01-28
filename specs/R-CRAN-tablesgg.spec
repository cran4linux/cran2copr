%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tablesgg
%global packver   0.9-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.1
Release:          1%{?dist}%{?buildtag}
Summary:          Presentation-Quality Tables, Displayed Using 'ggplot2'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-tables 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-grid 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-tables 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-grid 

%description
Presentation-quality tables are displayed as plots on an R graphics
device.  Although there are other packages that format tables for display,
this package is unique in combining two features: (a) It is aware of the
logical structure of the table being presented, and makes use of that for
automatic layout and styling of the table.  This avoids the need for most
manual adjustments to achieve an attractive result. (b) It displays tables
using 'ggplot2' graphics.  Therefore a table can be presented anywhere a
graph could be, with no more effort.  External software such as LaTeX or
HTML or their viewers is not required.  The package provides a full set of
tools to control the style and appearance of tables, including titles,
footnotes and reference marks, horizontal and vertical rules, and spacing
of rows and columns.  Methods are included to display matrices; data
frames; tables created by R's ftable(), table(), and xtabs() functions;
and tables created by the 'tables' and 'xtable' packages.  Methods can be
added to display other table-like objects.  A vignette is included that
illustrates usage and options available in the package.

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
