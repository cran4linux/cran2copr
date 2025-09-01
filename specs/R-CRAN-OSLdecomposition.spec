%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OSLdecomposition
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Signal Component Analysis for Optically Stimulated Luminescence

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3
Requires:         R-core >= 4.3
BuildArch:        noarch
BuildRequires:    R-CRAN-Luminescence >= 1.1.0
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-DEoptim 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-rmarkdown 
Requires:         R-CRAN-Luminescence >= 1.1.0
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-CRAN-DEoptim 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-rmarkdown 

%description
Function library for the identification and separation of exponentially
decaying signal components in continuous-wave optically stimulated
luminescence measurements. A special emphasis is laid on luminescence
dating with quartz, which is known for systematic errors due to signal
components with unequal physical behaviour. Also, this package enables an
easy to use signal decomposition of data sets imported and analysed with
the R package 'Luminescence'. This includes the optional automatic
creation of HTML reports. Further information and tutorials can be found
at <https://luminescence.de>.

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
