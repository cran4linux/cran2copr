%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dsos
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Dataset Shift with Outlier Scores

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats >= 3.6.1
BuildRequires:    R-CRAN-ggplot2 >= 3.3.3
BuildRequires:    R-CRAN-simctest >= 2.6
BuildRequires:    R-CRAN-future.apply >= 1.9.0
BuildRequires:    R-CRAN-data.table >= 1.14.0
BuildRequires:    R-CRAN-scales >= 1.1.1
Requires:         R-stats >= 3.6.1
Requires:         R-CRAN-ggplot2 >= 3.3.3
Requires:         R-CRAN-simctest >= 2.6
Requires:         R-CRAN-future.apply >= 1.9.0
Requires:         R-CRAN-data.table >= 1.14.0
Requires:         R-CRAN-scales >= 1.1.1

%description
Test for no adverse shift in two-sample comparison when we have a training
set, the reference distribution, and a test set. The approach is flexible
(extensible) and relies on a robust and powerful test statistic, the
weighted AUC. See Kamulete, V. M. (2021) <arXiv:2107.02990> for details.
Outlier scores such as trust scores and prediction uncertainty can be used
as the basis for comparison for example.

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
