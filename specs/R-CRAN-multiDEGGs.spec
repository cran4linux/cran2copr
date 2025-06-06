%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  multiDEGGs
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Omic Differentially Expressed Gene-Gene Pairs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-pbmcapply 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-sfsmisc 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-visNetwork 
Requires:         R-CRAN-DT 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-pbmcapply 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-sfsmisc 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-visNetwork 

%description
Performs multi-omic differential network analysis by revealing
differential interactions between molecular entities (genes, proteins,
transcription factors, or other biomolecules) across the omic datasets
provided. For each omic dataset, a differential network is constructed
where links represent statistically significant differential interactions
between entities. These networks are then integrated into a comprehensive
visualization using distinct colors to distinguish interactions from
different omic layers. This unified display allows interactive exploration
of cross-omic patterns, such as differential interactions present at both
transcript and protein levels. For each link, users can access
differential statistical significance metrics (p values or adjusted p
values, calculated via robust or traditional linear regression with
interaction term) and differential regression plots. The methods
implemented in this package are described in Sciacca et al. (2023)
<doi:10.1093/bioinformatics/btad192>.

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
