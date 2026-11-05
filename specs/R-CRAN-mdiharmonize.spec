%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mdiharmonize
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Harmonize Confidential Firm-Level Microdata into a Common Format

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mditools >= 0.1.1
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-mditools >= 0.1.1
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-grDevices 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-openxlsx 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-tools 
Requires:         R-utils 

%description
Harmonizes confidential firm-level microdata held at national statistical
institutes into one common structure, so that the same analysis code runs
unchanged in every country. Metadata tables describe each institute's raw
files and map their variables to the common ones; the functions read the
raw files, apply the mapping (revaluing, recoding, reclassifying,
redefining and remapping), make industry, product and regional
classifications consistent over time, switch between enterprise, firm and
plant identifiers, and add capital stocks computed with the perpetual
inventory method. Quality checks on the harmonized data report duplicate
keys, type conversion losses, breaks in yearly statistics and jumps in
missing values, and outputs pass statistical disclosure control before
they leave the institute. Builds on the analysis tools in 'mditools'.
Capital stocks via the perpetual inventory method follow OECD (2009)
<doi:10.1787/9789264068476-en>; disclosure control applies the
minimum-frequency and dominance rules with secondary suppression described
in Hundepool et al. (2012) <doi:10.1002/9781118348239>.

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
