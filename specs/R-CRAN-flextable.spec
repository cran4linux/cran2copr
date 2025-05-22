%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  flextable
%global packver   0.9.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.8
Release:          1%{?dist}%{?buildtag}
Summary:          Functions for Tabular Reporting

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rmarkdown >= 2.0
BuildRequires:    R-CRAN-data.table >= 1.13.0
BuildRequires:    R-CRAN-officer >= 0.6.7
BuildRequires:    R-CRAN-gdtools >= 0.4.0
BuildRequires:    R-CRAN-uuid >= 0.1.4
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-ragg 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-rmarkdown >= 2.0
Requires:         R-CRAN-data.table >= 1.13.0
Requires:         R-CRAN-officer >= 0.6.7
Requires:         R-CRAN-gdtools >= 0.4.0
Requires:         R-CRAN-uuid >= 0.1.4
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-ragg 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-xml2 

%description
Use a grammar for creating and customizing pretty tables. The following
formats are supported: 'HTML', 'PDF', 'RTF', 'Microsoft Word', 'Microsoft
PowerPoint' and R 'Grid Graphics'.  'R Markdown', 'Quarto' and the package
'officer' can be used to produce the result files. The syntax is the same
for the user regardless of the type of output to be produced. A set of
functions allows the creation, definition of cell arrangement, addition of
headers or footers, formatting and definition of cell content with text
and or images. The package also offers a set of high-level functions that
allow tabular reporting of statistical models and the creation of complex
cross tabulations.

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
