%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MultiObjMatch
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Objective Matching Algorithm

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cobalt 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-optmatch 
BuildRequires:    R-CRAN-matchMulti 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-rcbalance 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rlemon 
Requires:         R-CRAN-cobalt 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-optmatch 
Requires:         R-CRAN-matchMulti 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-rcbalance 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-utils 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rlemon 

%description
Matching algorithm based on network-flow structure. Users are able to
modify the emphasis on three different optimization goals: two different
distance measures and the number of treated units left unmatched. The
method is proposed by Pimentel and Kelz (2019)
<doi:10.1080/01621459.2020.1720693>. The 'rrelaxiv' package, which
provides an alternative solver for the underlying network flow problems,
carries an academic license and is not available on CRAN, but may be
downloaded from Github at <https://github.com/josherrickson/rrelaxiv/>.

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
