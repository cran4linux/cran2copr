%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DNNSIM
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Single-Index Neural Network for Skewed Heavy-Tailed Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats >= 4.3.0
BuildRequires:    R-CRAN-Rdpack >= 2.6
BuildRequires:    R-CRAN-reticulate >= 1.37.0
Requires:         R-stats >= 4.3.0
Requires:         R-CRAN-Rdpack >= 2.6
Requires:         R-CRAN-reticulate >= 1.37.0

%description
Provides a deep neural network model with a monotonic increasing single
index function tailored for periodontal disease studies. The residuals are
assumed to follow a skewed T distribution, a skewed normal distribution,
or a normal distribution. More details can be found at Liu, Huang, and Bai
(2024) <doi:10.1016/j.csda.2024.108012>.

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
