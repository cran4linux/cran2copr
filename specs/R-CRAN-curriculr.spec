%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  curriculr
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Data-Driven CVs with 'Quarto' and 'Typst'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-quarto 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-openxlsx2 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-quarto 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-openxlsx2 

%description
Provides tools for producing data-driven curriculum vitae documents from
structured data stored in an Excel workbook. The core workflow reads CV
content from a workbook, converts it into 'Typst' layout blocks, and
renders a polished PDF via the 'Quarto' publishing system. Includes
functions for reading and cleaning CV data, building 'Typst' section
headings and entries, rendering CV sections from data frames, and
scaffolding new CV projects with a standard folder structure and template
workbook. Designed to separate content from layout: CV data lives in the
spreadsheet, rendering configuration lives in 'Quarto', and transformation
logic lives in small, reusable R functions. See the 'Typst' typesetting
system at <https://typst.app> and the 'Quarto' publishing system at
<https://quarto.org>. Inspired by the 'vitae' package
<https://CRAN.R-project.org/package=vitae> and the 'Awesome CV' LaTeX
template <https://github.com/posquit0/Awesome-CV>.

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
