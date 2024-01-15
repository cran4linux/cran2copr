%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  miniMeta
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Web Application to Run Meta-Analyses

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-meta >= 7.0.0
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-rhandsontable 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-CRAN-WriteXLS 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-meta >= 7.0.0
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-rhandsontable 
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-markdown 
Requires:         R-CRAN-WriteXLS 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-jsonlite 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-stats 

%description
Shiny web application to run meta-analyses. Essentially a graphical
front-end to package 'meta' for R. Can be useful as an educational tool,
and for quickly analyzing and sharing meta-analyses. Provides output to
quickly fill in GRADE (Grading of Recommendations, Assessment, Development
and Evaluations) Summary-of-Findings tables. Importantly, it allows
further processing of the results inside R, in case more specific analyses
are needed.

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
