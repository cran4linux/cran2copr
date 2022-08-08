%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  aRchi
%global packver   2.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.2
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
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-VoxR 
BuildRequires:    R-CRAN-fastcluster 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-pkgcond 
BuildRequires:    R-CRAN-R.matlab 
BuildRequires:    R-CRAN-svMisc 
BuildRequires:    R-CRAN-circular 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-rgl 
Requires:         R-methods 
Requires:         R-CRAN-lidR 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-DiceKriging 
Requires:         R-CRAN-stringr 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-VoxR 
Requires:         R-CRAN-fastcluster 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-pkgcond 
Requires:         R-CRAN-R.matlab 
Requires:         R-CRAN-svMisc 
Requires:         R-CRAN-circular 

%description
Provides a set of tools to make quantitative structural model of trees
(i.e the so-called 'QSM') from LiDAR point cloud, to manipulate and
visualize the QSMs as well as to compute metrics from them. It can be used
in various context of forest ecology (i.e biomass estimation) and tree
architecture (i.e architectural metrics), see Martin-Ducup et al. (2020)
<doi:10.1111/1365-2435.13678>. The package is based on a new S4 class
called 'aRchi'.

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
