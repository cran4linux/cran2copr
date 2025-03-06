%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  REDCapCAST
%global packver   25.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          25.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          REDCap Metadata Casting and Castellated Data Handling

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-REDCapR 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-keyring 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-zip 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-gt 
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-here 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-gtsummary 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-openxlsx2 
BuildRequires:    R-CRAN-readODS 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-REDCapR 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-keyring 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-stats 
Requires:         R-CRAN-zip 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-gt 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-here 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-gtsummary 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-openxlsx2 
Requires:         R-CRAN-readODS 

%description
Casting metadata for REDCap database creation and handling of castellated
data using repeated instruments and longitudinal projects in 'REDCap'.
Keeps a focused data export approach, by allowing to only export required
data from the database. Also for casting new REDCap databases based on
datasets from other sources. Originally forked from the R part of
'REDCapRITS' by Paul Egeler. See <https://github.com/pegeler/REDCapRITS>.
'REDCap' (Research Electronic Data Capture) is a secure, web-based
software platform designed to support data capture for research studies,
providing 1) an intuitive interface for validated data capture; 2) audit
trails for tracking data manipulation and export procedures; 3) automated
export procedures for seamless data downloads to common statistical
packages; and 4) procedures for data integration and interoperability with
external sources (Harris et al (2009) <doi:10.1016/j.jbi.2008.08.010>;
Harris et al (2019) <doi:10.1016/j.jbi.2019.103208>).

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
