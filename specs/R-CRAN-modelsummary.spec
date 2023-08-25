%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  modelsummary
%global packver   1.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Summary Tables and Plots for Statistical Models and Data: Beautiful, Customizable, and Publication-Ready

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate >= 2.1.0
BuildRequires:    R-CRAN-kableExtra >= 1.3.4
BuildRequires:    R-CRAN-tables >= 0.9.10
BuildRequires:    R-CRAN-parameters >= 0.21.0
BuildRequires:    R-CRAN-insight >= 0.19.1
BuildRequires:    R-CRAN-performance >= 0.10.2
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-glue 
Requires:         R-CRAN-checkmate >= 2.1.0
Requires:         R-CRAN-kableExtra >= 1.3.4
Requires:         R-CRAN-tables >= 0.9.10
Requires:         R-CRAN-parameters >= 0.21.0
Requires:         R-CRAN-insight >= 0.19.1
Requires:         R-CRAN-performance >= 0.10.2
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-glue 

%description
Create beautiful and customizable tables to summarize several statistical
models side-by-side. Draw coefficient plots, multi-level cross-tabs,
dataset summaries, balance tables (a.k.a. "Table 1s"), and correlation
matrices. This package supports dozens of statistical models, and it can
produce tables in HTML, LaTeX, Word, Markdown, PDF, PowerPoint, Excel,
RTF, JPG, or PNG. Tables can easily be embedded in 'Rmarkdown' or 'knitr'
dynamic documents. Details can be found in Arel-Bundock (2022)
<doi:10.18637/jss.v103.i01>.

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
