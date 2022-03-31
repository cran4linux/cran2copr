%global __brp_check_rpaths %{nil}
%global packname  svrep
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Creating, Updating, and Analyzing Survey Replicate Weights

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-survey >= 4.1
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-survey >= 4.1
Requires:         R-stats 
Requires:         R-utils 

%description
Provides tools for creating and working with survey replicate weights,
extending functionality of the 'survey' package from Lumley (2004)
<doi:10.18637/jss.v009.i08>. Methods are provided for applying nonresponse
adjustments to both full-sample and replicate weights as suggested by Rust
and Rao (1996) <doi:10.1177/096228029600500305> in order to account for
the impact of these adjustments on sampling variances. Diagnostic
functions are included to compare weights and weighted estimates from
different sets of replicate weights.

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
