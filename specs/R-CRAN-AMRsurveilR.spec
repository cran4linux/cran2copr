%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AMRsurveilR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Antimicrobial Resistance Surveillance, Epidemiology and Risk Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-spdep 
Requires:         R-stats 

%description
Provides tools for antimicrobial resistance surveillance, epidemiological
analysis, temporal trend detection, early warning detection, spatial
cluster identification, and risk factor analysis. The package supports
analysis of antimicrobial resistance patterns, resistance to multiple
antimicrobial classes, temporal surveillance, and spatial epidemiology for
applications in veterinary, medical, and One Health research.
Antimicrobial resistance surveillance approaches are informed by
guidelines from WHO (2023)
<https://www.who.int/publications/i/item/9789240076600> and WOAH (2024)
<https://www.woah.org/fileadmin/Home/eng/Health_standards/tahc/2024/en_chapitre_antibio_harmonisation.htm>.
Statistical methods include cumulative sum (CUSUM) monitoring (Page, 1954)
<doi:10.1093/biomet/41.1-2.100>, exponentially weighted moving average
(EWMA) monitoring (Roberts, 1959) <doi:10.1080/00401706.1959.10489860>,
Local Moran's I spatial analysis (Anselin, 1995)
<doi:10.1111/j.1538-4632.1995.tb00338.x>, and multidrug- and extensively
drug-resistant classification (Magiorakos et al., 2012)
<doi:10.1111/j.1469-0691.2011.03570.x>.

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
