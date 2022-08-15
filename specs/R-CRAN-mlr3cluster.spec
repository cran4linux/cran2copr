%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mlr3cluster
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Cluster Extension for 'mlr3'

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-backports >= 1.1.10
BuildRequires:    R-CRAN-mlr3misc >= 0.9.4
BuildRequires:    R-CRAN-mlr3 >= 0.14.0
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-CRAN-clusterCrit 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-paradox 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-stats 
Requires:         R-CRAN-backports >= 1.1.10
Requires:         R-CRAN-mlr3misc >= 0.9.4
Requires:         R-CRAN-mlr3 >= 0.14.0
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-clue 
Requires:         R-CRAN-clusterCrit 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-paradox 
Requires:         R-CRAN-R6 
Requires:         R-stats 

%description
Extends the 'mlr3' package with cluster analysis.

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
