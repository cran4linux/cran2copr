%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RobustANOVA
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Robust One-Way ANOVA Tests under Heteroscedasticity and Nonnormality

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-PEIP 
BuildRequires:    R-CRAN-optimbase 
Requires:         R-stats 
Requires:         R-CRAN-PEIP 
Requires:         R-CRAN-optimbase 

%description
Robust tests (RW, RPB and RGF) are provided for testing the equality of
several long-tailed symmetric (LTS) means when the variances are unknown
and arbitrary. RW, RPB and RGF tests are robust versions of Welch's F test
proposed by Welch (1951) <doi:10.2307/2332579>, parametric bootstrap test
proposed by Krishnamoorthy et. al (2007) <doi:10.1016/j.csda.2006.09.039>;
and generalized F test proposed by Weerahandi (1995)
<doi:10.2307/2532947>;, respectively. These tests are based on the
modified maximum likelihood (MML) estimators proposed by Tiku(1967, 1968)
<doi:10.2307/2333859>, <doi:10.1080/01621459.1968.11009228>.

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
