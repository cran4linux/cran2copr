%global __brp_check_rpaths %{nil}
%global packname  colorBlindness
%global packver   0.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.9
Release:          1%{?dist}%{?buildtag}
Summary:          Safe Color Set for Color Blindness

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-gridGraphics 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-grid 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-colorspace 
Requires:         R-graphics 
Requires:         R-CRAN-gridGraphics 
Requires:         R-CRAN-gtable 
Requires:         R-grid 

%description
Provide the safe color set for color blindness, the simulator of
protanopia, deuteranopia. The color sets are collected from: Wong, B.
(2011) <doi:10.1038/nmeth.1618>, and <http://mkweb.bcgsc.ca/biovis2012/>.
The simulations of the appearance of the colors to color-deficient viewers
were based on algorithms in Vienot, F., Brettel, H. and Mollon, J.D.
(1999)
<doi:10.1002/(SICI)1520-6378(199908)24:4%%3C243::AID-COL5%%3E3.0.CO;2-3>.
The cvdPlot() function to generate 'ggplot' grobs of simulations were
modified from <https://github.com/clauswilke/colorblindr>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
