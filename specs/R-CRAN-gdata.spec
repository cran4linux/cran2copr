%global __brp_check_rpaths %{nil}
%global packname  gdata
%global packver   2.18.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.18.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Various R Programming Tools for Data Manipulation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         perl >= 5.10.0
BuildRequires:    R-devel >= 2.3.0
Requires:         R-core >= 2.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-gtools 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-utils 

%description
Various R programming tools for data manipulation, including: - medical
unit conversions ('ConvertMedUnits', 'MedUnits'), - combining objects
('bindData', 'cbindX', 'combine', 'interleave'), - character vector
operations ('centerText', 'startsWith', 'trim'), - factor manipulation
('levels', 'reorder.factor', 'mapLevels'), - obtaining information about R
objects ('object.size', 'elem', 'env', 'humanReadable', 'is.what', 'll',
'keep', 'ls.funs', 'Args','nPairs', 'nobs'), - manipulating MS-Excel
formatted files ('read.xls', 'installXLSXsupport', 'sheetCount',
'xlsFormats'), - generating fixed-width format files ('write.fwf'), -
extricating components of date & time objects ('getYear', 'getMonth',
'getDay', 'getHour', 'getMin', 'getSec'), - operations on columns of data
frames ('matchcols', 'rename.vars'), - matrix operations ('unmatrix',
'upperTriangle', 'lowerTriangle'), - operations on vectors ('case',
'unknownToNA', 'duplicated2', 'trimSum'), - operations on data frames
('frameApply', 'wideByFactor'), - value of last evaluated expression
('ans'), and - wrapper for 'sample' that ensures consistent behavior for
both scalar and vector arguments ('resample').

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
