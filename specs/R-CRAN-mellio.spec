%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mellio
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Polished, Editable Tables and Statistical Results

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-broom >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-gt >= 0.10.0
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-methods 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-broom >= 1.0.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-gt >= 0.10.0
Requires:         R-CRAN-jsonlite 
Requires:         R-methods 

%description
Sends supported 'R' objects to the 'Mellio' web app and creates polished,
editable statistical tables in 'R'. The 'mellio_open' interface handles
common hypothesis tests, model objects, model comparisons, descriptive
summaries, tabular data, plots, and image files. The 'melliotab' interface
formats data frames, model summaries, correlation matrices, and
side-by-side comparison tables with APA-style numeric formatting,
confidence intervals, table notes, and optional significance markers.
Manual table helpers can copy or save 'melliotab' output as 'HTML',
'LaTeX', or 'Markdown' when file-based handoff is needed. Payloads include
package-version metadata to support reproducible reporting and software
citation.

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
