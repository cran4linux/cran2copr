%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  visvow
%global packver   1.3.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.7
Release:          1%{?dist}%{?buildtag}
Summary:          Visible Vowels: Visualization of Vowel Variation

License:          GNU General Public License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-PBSmapping 
BuildRequires:    R-CRAN-splitstackshape 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-formattable 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-ggdendro 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-WriteXLS 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-svglite 
BuildRequires:    R-CRAN-Cairo 
BuildRequires:    R-CRAN-tikzDevice 
BuildRequires:    R-CRAN-shinybusy 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-PBSmapping 
Requires:         R-CRAN-splitstackshape 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-formattable 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-ggdendro 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-WriteXLS 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-Rtsne 
Requires:         R-grid 
Requires:         R-CRAN-svglite 
Requires:         R-CRAN-Cairo 
Requires:         R-CRAN-tikzDevice 
Requires:         R-CRAN-shinybusy 
Requires:         R-CRAN-Rdpack 

%description
Visualizes vowel variation in f0, F1, F2, F3 and duration.

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
