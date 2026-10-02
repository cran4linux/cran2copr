%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FAfA
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Factor Analysis for All

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-EGAnet >= 2.4.1
BuildRequires:    R-CRAN-Amelia 
BuildRequires:    R-CRAN-EFA.MRFA 
BuildRequires:    R-CRAN-ItemRest 
BuildRequires:    R-CRAN-bsicons 
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-golem 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-missForest 
BuildRequires:    R-CRAN-mvnormalTest 
BuildRequires:    R-CRAN-naniar 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-semPlot 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-EGAnet >= 2.4.1
Requires:         R-CRAN-Amelia 
Requires:         R-CRAN-EFA.MRFA 
Requires:         R-CRAN-ItemRest 
Requires:         R-CRAN-bsicons 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-golem 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-missForest 
Requires:         R-CRAN-mvnormalTest 
Requires:         R-CRAN-naniar 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-qgraph 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-semPlot 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Provides a comprehensive Shiny-based graphical user interface for
conducting a wide range of factor analysis procedures. 'FAfA' (Factor
Analysis for All) guides users through data uploading, assumption checking
(descriptive statistics, collinearity, multivariate normality, outliers),
data wrangling (variable exclusion, data splitting), exploratory factor
analysis (EFA) with various rotation and extraction methods, confirmatory
factor analysis (CFA), reliability analysis (e.g., Cronbach's Alpha,
McDonald's Omega), and measurement invariance testing across groups.
Factor retention methods include parallel analysis following Horn (1965)
<doi:10.1007/BF02289447>, optimized parallel analysis following Timmerman
and Lorenzo-Seva (2011) <doi:10.1037/a0023353>, permutation parallel
analysis for categorical variables following Lubbe (2019)
<doi:10.1037/met0000171>, the Hull method following Lorenzo-Seva et al.
(2011) <doi:10.1080/00273171.2011.564527>, minimum average partial
criteria following Velicer (1976) <doi:10.1007/BF02293557> and O'Connor
(2000) <doi:10.3758/BF03200807>, and the empirical Kaiser criterion
following Braeken and van Assen (2017) <doi:10.1037/met0000074>.
Exploratory graph analysis follows Golino and Epskamp (2017)
<doi:10.1371/journal.pone.0174035>, with bootstrap stability assessment
following Christensen and Golino (2021) <doi:10.3390/psych3030032>.
Internal split-sample EFA replication follows Osborne and Fitzpatrick
(2012) <doi:10.7275/h0bd-4d11>. Model-specific dynamic fit index cutoffs
for CFA follow McNeish and Wolf (2023) <doi:10.1037/met0000425>. Item
weighting follows Kılıç (2026) <doi:10.3758/s13428-026-03095-w>. Analyses
use established R packages such as 'lavaan' and 'psych'. Results are
presented in tables and plots with downloadable outputs. Analysis projects
can be saved and restored, and reproducible R, HTML, and PDF workflow
reports can be generated.

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
