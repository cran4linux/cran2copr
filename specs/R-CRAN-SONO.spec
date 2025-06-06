%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SONO
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Scores of Nominal Outlyingness (SONO)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-Rdpack >= 2.0
BuildRequires:    R-CRAN-data.table >= 1.14.0
BuildRequires:    R-CRAN-DescTools >= 0.99.0
BuildRequires:    R-CRAN-rje >= 0.9
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-Rdpack >= 2.0
Requires:         R-CRAN-data.table >= 1.14.0
Requires:         R-CRAN-DescTools >= 0.99.0
Requires:         R-CRAN-rje >= 0.9

%description
Computes scores of outlyingness for data sets consisting of nominal
variables and includes various evaluation metrics for assessing
performance of outlier identification algorithms producing scores of
outlyingness. The scores of nominal outlyingness are computed based on the
framework of Costa and Papatsouma (2025) <doi:10.48550/arXiv.2408.07463>.

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
