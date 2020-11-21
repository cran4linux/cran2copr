%global packname  HeckmanEM
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fit Normal or Student-t Heckman Selection Models

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MomTrunc >= 5.79
BuildRequires:    R-CRAN-PerformanceAnalytics >= 2.0.4
BuildRequires:    R-CRAN-sampleSelection >= 1.2.6
BuildRequires:    R-CRAN-mvtnorm >= 1.1.0
Requires:         R-CRAN-MomTrunc >= 5.79
Requires:         R-CRAN-PerformanceAnalytics >= 2.0.4
Requires:         R-CRAN-sampleSelection >= 1.2.6
Requires:         R-CRAN-mvtnorm >= 1.1.0

%description
Maximum likelihood estimation by an EM algorithm of Heckman-type sample
selection Normal or Student-t models. The reference is Lachos, Prates and
Dey (2020) <arXiv:2006.08036>.

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
