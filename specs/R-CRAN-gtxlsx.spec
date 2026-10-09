%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gtxlsx
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Write 'gt' and HTML Tables into 'openxlsx2' Workbooks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-openxlsx2 >= 1.0
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-CRAN-openxlsx2 >= 1.0
Requires:         R-grDevices 
Requires:         R-utils 

%description
Turns a 'gt' table into a range of cells in an 'openxlsx2' workbook,
keeping the heading, column spanners, row groups, stub, summary rows,
footnotes and the styling set through 'gt'. Numbers stay numbers wherever
a spreadsheet number format can reproduce what 'gt' shows. A second entry
point does the same for a plain HTML table, so output from other table
packages can be written to a worksheet as well; that path needs nothing
beyond 'openxlsx2'.

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
