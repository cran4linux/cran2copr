%global packname  gemtc
%global packver   1.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Network Meta-Analysis Using Bayesian Methods

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-rjags >= 4.0
BuildRequires:    R-CRAN-meta >= 2.1
BuildRequires:    R-CRAN-plyr >= 1.8
BuildRequires:    R-CRAN-igraph >= 1.0
BuildRequires:    R-CRAN-forcats >= 0.5.0
BuildRequires:    R-CRAN-coda >= 0.13
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-Rglpk 
Requires:         R-CRAN-rjags >= 4.0
Requires:         R-CRAN-meta >= 2.1
Requires:         R-CRAN-plyr >= 1.8
Requires:         R-CRAN-igraph >= 1.0
Requires:         R-CRAN-forcats >= 0.5.0
Requires:         R-CRAN-coda >= 0.13
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grid 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-Rglpk 

%description
Network meta-analyses (mixed treatment comparisons) in the Bayesian
framework using JAGS. Includes methods to assess heterogeneity and
inconsistency, and a number of standard visualizations. van Valkenhoef et
al. (2012) <doi:10.1002/jrsm.1054>; van Valkenhoef et al. (2015)
<doi:10.1002/jrsm.1167>.

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
