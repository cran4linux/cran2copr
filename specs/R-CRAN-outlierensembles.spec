%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  outlierensembles
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          A Collection of Outlier Ensemble Algorithms

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-airt 
BuildRequires:    R-CRAN-EstCRM 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-apcluster 
Requires:         R-CRAN-airt 
Requires:         R-CRAN-EstCRM 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-apcluster 

%description
Ensemble functions for outlier/anomaly detection. There is a new ensemble
method proposed using Item Response Theory. Existing outlier ensemble
methods from Schubert et al (2012) <doi:10.1137/1.9781611972825.90>,
Chiang et al (2017) <doi:10.1016/j.jal.2016.12.002> and Aggarwal and Sathe
(2015) <doi:10.1145/2830544.2830549> are also included.

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
