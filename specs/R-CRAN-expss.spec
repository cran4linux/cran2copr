%global packname  expss
%global packver   0.10.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.6
Release:          1%{?dist}%{?buildtag}
Summary:          Tables, Labels and Some Useful Functions from Spreadsheets and'SPSS' Statistics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-htmlTable >= 1.11.0
BuildRequires:    R-CRAN-data.table >= 1.10
BuildRequires:    R-CRAN-matrixStats >= 0.51.0
BuildRequires:    R-foreign 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-htmlTable >= 1.11.0
Requires:         R-CRAN-data.table >= 1.10
Requires:         R-CRAN-matrixStats >= 0.51.0
Requires:         R-foreign 
Requires:         R-utils 
Requires:         R-stats 

%description
Package computes and displays tables with support for 'SPSS'-style labels,
multiple and nested banners, weights, multiple-response variables and
significance testing. There are facilities for nice output of tables in
'knitr', 'Shiny', '*.xlsx' files, R and 'Jupyter' notebooks. Methods for
labelled variables add value labels support to base R functions and to
some functions from other packages. Additionally, the package brings
popular data transformation functions from 'SPSS' Statistics and 'Excel':
'RECODE', 'COUNT', 'COMPUTE', 'DO IF', 'COUNTIF', 'VLOOKUP' and etc. These
functions are very useful for data processing in marketing research
surveys. Package intended to help people to move data processing from
'Excel' and 'SPSS' to R.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
