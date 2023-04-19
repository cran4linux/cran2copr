%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  knitxl
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generates a Spreadsheet Report from an 'rmarkdown' File

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-openxlsx >= 4.2.5
BuildRequires:    R-CRAN-R6 >= 2.5.1
BuildRequires:    R-CRAN-yaml >= 2.3.7
BuildRequires:    R-CRAN-readr >= 2.1.2
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-commonmark >= 1.8.0
BuildRequires:    R-CRAN-glue >= 1.6.2
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-knitr >= 1.39
BuildRequires:    R-CRAN-xml2 >= 1.3.3
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-readbitmap >= 0.1.5
Requires:         R-CRAN-openxlsx >= 4.2.5
Requires:         R-CRAN-R6 >= 2.5.1
Requires:         R-CRAN-yaml >= 2.3.7
Requires:         R-CRAN-readr >= 2.1.2
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-commonmark >= 1.8.0
Requires:         R-CRAN-glue >= 1.6.2
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-knitr >= 1.39
Requires:         R-CRAN-xml2 >= 1.3.3
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-readbitmap >= 0.1.5

%description
Convert an R Markdown documents into an '.xlsx' spreadsheet reports with
the knitxl() function, which works similarly to knit() from the 'knitr'
package. The generated report can be opened in 'Excel' or similar software
for further analysis and presentation.

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
