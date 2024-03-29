%global __brp_check_rpaths %{nil}
%global packname  BatchExperiments
%global packver   1.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Experiments on Batch Computing Clusters

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RSQLite >= 2.0
BuildRequires:    R-CRAN-data.table >= 1.9.6
BuildRequires:    R-CRAN-checkmate >= 1.8.5
BuildRequires:    R-CRAN-BatchJobs >= 1.7
BuildRequires:    R-CRAN-BBmisc >= 1.11
BuildRequires:    R-CRAN-backports 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-DBI 
Requires:         R-CRAN-RSQLite >= 2.0
Requires:         R-CRAN-data.table >= 1.9.6
Requires:         R-CRAN-checkmate >= 1.8.5
Requires:         R-CRAN-BatchJobs >= 1.7
Requires:         R-CRAN-BBmisc >= 1.11
Requires:         R-CRAN-backports 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-DBI 

%description
Extends the BatchJobs package to run statistical experiments on batch
computing clusters. For further details see the project web page.

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
