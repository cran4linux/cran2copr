%global packname  idiogramFISH
%global packver   2.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Shiny App. Idiograms with Marks and Karyotype Indices

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 

%description
Plot idiograms of karyotypes, plasmids, circular chr. having a set of
data.frames for chromosome data and optionally mark data. Two styles of
chromosomes can be used: without or with visible chromatids (when not
circular). Supports micrometers, cM and Mb or any unit. Three styles of
centromeres are available: triangular, rounded and inProtein; and six
styles of marks are available: square (squareLeft), dots, cM (cMLeft),
cenStyle, upArrow (downArrow), exProtein (inProtein); its legend (label)
can be drawn inline or to the right of karyotypes. Idiograms can also be
plotted in concentric circles. It is possible to calculate chromosome
indices by Levan et al. (1964) <doi:10.1111/j.1601-5223.1964.tb01953.x>,
karyotype indices of Watanabe et al. (1999) <doi:10.1007/PL00013869> and
Romero-Zarco (1986) <doi:10.2307/1221906> and classify chromosomes by
morphology Guerra (1986) and Levan et al. (1964).

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
