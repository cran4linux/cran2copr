%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Familia
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          'shiny' Application for Population Structure and Ancestry Assessments

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-vcfR >= 1.15.0
BuildRequires:    R-CRAN-BIGpopA 
BuildRequires:    R-CRAN-bs4Dash 
BuildRequires:    R-CRAN-config 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-golem 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydisconnect 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-zip 
Requires:         R-CRAN-vcfR >= 1.15.0
Requires:         R-CRAN-BIGpopA 
Requires:         R-CRAN-bs4Dash 
Requires:         R-CRAN-config 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-golem 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydisconnect 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-zip 

%description
Provides a 'shiny' web application developed by the Breeding Insight team
to support pedigree validation and ancestry assessment of plant and animal
populations. The app integrates Mendelian error analysis, parentage
assignment and genetic composition/ancestry methods to help researchers
evaluate genomic relationships through an accessible, web-based interface
without requiring command-line tools. Pedigree validation, Mendelian error
analysis and parentage assignment build on the 'BIGpopA' package
(<https://CRAN.R-project.org/package=BIGpopA>). Ancestry estimation uses
the sparse non-negative matrix factorization method of Frichot et al.
(2014) <doi:10.1534/genetics.113.160572> as implemented in the 'LEA'
package by Frichot and Francois (2015) <doi:10.1111/2041-210X.12382>. Line
and breed composition are estimated using the breed composition regression
method of Funkhouser et al. (2017) <doi:10.2527/tas2016.0003>, extended to
polyploid species by Sandercock et al. (2025) <doi:10.1002/tpg2.70067>.

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
