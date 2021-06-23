%global __brp_check_rpaths %{nil}
%global packname  aRchi
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Quantitative Structural Model ('QSM') Treatment for Tree Architecture

License:          CeCILL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lidR 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-DiceKriging 
BuildRequires:    R-CRAN-circular 
BuildRequires:    R-CRAN-pkgcond 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-gtools 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-rgl 
Requires:         R-methods 
Requires:         R-CRAN-lidR 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-DiceKriging 
Requires:         R-CRAN-circular 
Requires:         R-CRAN-pkgcond 
Requires:         R-CRAN-stringr 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-gtools 

%description
Provides a set of tools to manipulate, visualize and compute metrics from
quantitative structural model of trees (i.e the so-called 'QSM') . It can
be used in various context of forest ecology (i.e biomass estimation) and
tree architecture (i.e architectural metrics), see Martin-Ducup et al.
(2020) <doi:10.1111/1365-2435.13678>. The package is based on a new S4
class called 'aRchi'.

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
