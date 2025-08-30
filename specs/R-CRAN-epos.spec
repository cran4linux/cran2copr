%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  epos
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Epilepsy Ontologies' Similarities

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-hash 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-TopKLists 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-mongolite 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-VennDiagram 
BuildRequires:    R-CRAN-cowplot 
Requires:         R-CRAN-hash 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-TopKLists 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-mongolite 
Requires:         R-stats 
Requires:         R-CRAN-VennDiagram 
Requires:         R-CRAN-cowplot 

%description
Analysis and visualization of similarities between epilepsy ontologies
based on text mining results by comparing ranked lists of co-occurring
drug terms in the BioASQ corpus. The ranked result lists of neurological
drug terms co-occurring with terms from the epilepsy ontologies EpSO,
ESSO, EPILONT, EPISEM and FENICS undergo further analysis. The source data
to create the ranked lists of drug names is produced using the text mining
workflows described in Mueller, Bernd and Hagelstein, Alexandra (2016)
<doi:10.4126/FRL01-006408558>, Mueller, Bernd et al. (2017)
<doi:10.1007/978-3-319-58694-6_22>, Mueller, Bernd and Rebholz-Schuhmann,
Dietrich (2020) <doi:10.1007/978-3-030-43887-6_52>, and Mueller, Bernd et
al. (2022) <doi:10.1186/s13326-021-00258-w>.

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
