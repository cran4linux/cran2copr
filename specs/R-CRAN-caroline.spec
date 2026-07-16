%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  caroline
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          A Collection of Database, Data Structure, Data Conversion, Visualization, Reporting, and General Utility Functions

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0.0
Requires:         R-core >= 2.0.0
BuildArch:        noarch
BuildRequires:    R-methods 
Requires:         R-methods 

%description
This R-extension package contains dozens of functions useful for: database
style joins [nerge()] & aggregation [bestBy(), groupBy() & regroup()],
database migration [dbWriteTable2()], file I/O [write.delim(),
read.tab()], text parsing / data mining [m()], data structure conversion
[nv(), tab2df()], summarizing & reporting [pct(), fit.1ln.rprt()],
character string manipulation [m() & pad()], legend table making
[sstable() & leghead()] & plot placement [legend.position()], plot
annotation [labsegs() & mvlabs()], data visualization [pies(), spie(), &
heatmatrix()], and data exploration [hyperplot(), plot.xy.ab.p()], batch
scripting [parseArgString()]. The package's greatest contributions stem
from its database style merge, aggregation and interface functions as well
as in it's extensive use and propagation of row, column and vector names
in most functions. The latest additions are plotting functions
[confound.grid() & sparge()] that intake a dataframe & formulas to
visually resolve variable confounding (Simpson, 1951).

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
