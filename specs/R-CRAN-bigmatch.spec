%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bigmatch
%global packver   0.6.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.4
Release:          1%{?dist}%{?buildtag}
Summary:          Making Optimal Matching Size-Scalable Using Optimal Calipers

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rcbalance 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-liqueueR 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-methods 
Requires:         R-CRAN-rcbalance 
Requires:         R-stats 
Requires:         R-CRAN-liqueueR 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-mvnfast 
Requires:         R-methods 

%description
Implements optimal matching with near-fine balance in large observational
studies with the use of optimal calipers to get a sparse network. The
caliper is optimal in the sense that it is as small as possible such that
a matching exists. The main functions in the 'bigmatch' package are
optcal() to find the optimal caliper, optconstant() to find the optimal
number of nearest neighbors, and nfmatch() to find a near-fine balance
match with a caliper and a restriction on the number of nearest neighbors.
Yu, R., Silber, J. H., and Rosenbaum, P. R. (2020).
<DOI:10.1214/19-sts699>.

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
