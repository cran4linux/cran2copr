%global packname  EMSS
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Some EM-Type Estimation Methods for the Heckman Selection Model

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-sampleSelection 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-sampleSelection 
Requires:         R-CRAN-mvtnorm 

%description
Some EM-type algorithms to estimate parameters for the well-known Heckman
selection model are provided in the package. Such algorithms are as
follow: ECM(Expectation/Conditional Maximization), ECM(NR)(the
Newton-Raphson method is adapted to the ECM) and
ECME(Expectation/Conditional Maximization Either). Since the algorithms
are based on the EM algorithm, they also have EM’s main advantages,
namely, stability and ease of implementation. Further details and
explanations of the algorithms can be found in Zhao et al. (2020) <doi:
10.1016/j.csda.2020.106930>.

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
