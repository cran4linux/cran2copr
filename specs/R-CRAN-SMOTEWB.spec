%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SMOTEWB
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Imbalanced Resampling using SMOTE with Boosting (SMOTEWB)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4
Requires:         R-core >= 4.4
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-Rfast 
Requires:         R-stats 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-Rfast 

%description
Provides the SMOTE with Boosting (SMOTEWB) algorithm. See F. Sağlam, M. A.
Cengiz (2022) <doi:10.1016/j.eswa.2022.117023>. It is a SMOTE-based
resampling technique which creates synthetic data on the links between
nearest neighbors. SMOTEWB uses boosting weights to determine where to
generate new samples and automatically decides the number of neighbors for
each sample. It is robust to noise and outperforms most of the
alternatives according to Matthew Correlation Coefficient metric.
Alternative resampling methods are also available in the package.

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
