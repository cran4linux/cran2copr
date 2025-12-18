%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OhdsiReportGenerator
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Observational Health Data Sciences and Informatics Report Generator

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-reactable >= 0.4.4
BuildRequires:    R-CRAN-CirceR 
BuildRequires:    R-CRAN-DatabaseConnector 
BuildRequires:    R-CRAN-forestplot 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-gt 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-ParallelLogger 
BuildRequires:    R-CRAN-quarto 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-reactable >= 0.4.4
Requires:         R-CRAN-CirceR 
Requires:         R-CRAN-DatabaseConnector 
Requires:         R-CRAN-forestplot 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-gt 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-ParallelLogger 
Requires:         R-CRAN-quarto 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
Extract results into R from the Observational Health Data Sciences and
Informatics result database (see
<https://ohdsi.github.io/Strategus/results-schema/index.html>) and
generate reports/presentations via 'quarto' that summarize results in HTML
format. Learn more about 'OhdsiReportGenerator' at
<https://ohdsi.github.io/OhdsiReportGenerator/>.

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
