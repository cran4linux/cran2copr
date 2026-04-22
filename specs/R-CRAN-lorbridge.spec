%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lorbridge
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bridging Log-Odds Ratios and Correspondence Analysis via Closeness-of-Concordance Measures

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-nnet >= 7.3
BuildRequires:    R-CRAN-CAvariants >= 5.5
BuildRequires:    R-stats 
Requires:         R-CRAN-nnet >= 7.3
Requires:         R-CRAN-CAvariants >= 5.5
Requires:         R-stats 

%description
Provides a unified analytical workflow that bridges conventional binary
and multinomial logistic regression with singly-ordered (SONSCA) and
doubly-ordered (DONSCA) nonsymmetric correspondence analysis. Log-odds
ratios (LORs) from logistic regression are re-expressed as cosine theta
estimates and closeness-of-concordance measures (CCMs) -- including Yule's
Q, Yule's Y, and r_meta -- on the familiar [-1, +1] scale introduced by
Kim and Grochowalski (2019) <doi:10.3758/s13428-018-1161-1>. Bootstrap
confidence intervals for cosine theta are provided throughout. The package
is intended to help clinical and medical researchers interpret association
strength from logistic regression in an intuitive, correlation-like
metric, and to connect conventional regression results with geometric
correspondence analysis visualisations.

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
