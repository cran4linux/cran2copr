%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cpmBigData
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fitting Semiparametric Cumulative Probability Models for Big Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rms >= 6.2.0
BuildRequires:    R-CRAN-Hmisc >= 4.3.0
BuildRequires:    R-parallel >= 3.5.2
BuildRequires:    R-CRAN-SparseM >= 1.77
BuildRequires:    R-CRAN-foreach >= 1.2.0
BuildRequires:    R-CRAN-benchmarkme >= 1.0.4
BuildRequires:    R-CRAN-doParallel >= 1.0.11
BuildRequires:    R-CRAN-iterators >= 1.0.0
Requires:         R-CRAN-rms >= 6.2.0
Requires:         R-CRAN-Hmisc >= 4.3.0
Requires:         R-parallel >= 3.5.2
Requires:         R-CRAN-SparseM >= 1.77
Requires:         R-CRAN-foreach >= 1.2.0
Requires:         R-CRAN-benchmarkme >= 1.0.4
Requires:         R-CRAN-doParallel >= 1.0.11
Requires:         R-CRAN-iterators >= 1.0.0

%description
A big data version for fitting cumulative probability models using the
orm() function from the 'rms' package.  See Liu et al. (2017)
<DOI:10.1002/sim.7433> for details.

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
