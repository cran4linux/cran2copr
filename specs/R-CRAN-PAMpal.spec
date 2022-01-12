%global __brp_check_rpaths %{nil}
%global packname  PAMpal
%global packver   0.15.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.15.0
Release:          1%{?dist}%{?buildtag}
Summary:          Load and Process Passive Acoustic Data

License:          GNU General Public License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-PamBinaries >= 1.3.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tuneR 
BuildRequires:    R-CRAN-seewave 
BuildRequires:    R-CRAN-gam 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-PAMmisc 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-manipulate 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-lubridate 
Requires:         R-CRAN-PamBinaries >= 1.3.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tuneR 
Requires:         R-CRAN-seewave 
Requires:         R-CRAN-gam 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-PAMmisc 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-purrr 
Requires:         R-methods 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-manipulate 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-lubridate 

%description
Tools for loading and processing passive acoustic data. Read in data that
has been processed in 'Pamguard' (<https://www.pamguard.org/>), apply a
suite processing functions, and export data for reports or external
modeling tools. Parameter calculations implement methods by Oswald et al
(2007) <doi:10.1121/1.2743157>, Griffiths et al (2020)
<doi:10.1121/10.0001229> and Baumann-Pickering et al (2010)
<doi:10.1121/1.3479549>.

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
