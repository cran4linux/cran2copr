%global __brp_check_rpaths %{nil}
%global packname  FuzzySTs
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Fuzzy Statistical Tools

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-FuzzyNumbers 
BuildRequires:    R-CRAN-polynom 
Requires:         R-CRAN-FuzzyNumbers 
Requires:         R-CRAN-polynom 

%description
The main goal of this package is to present various fuzzy statistical
tools. It intends to provide an implementation of the theoretical and
empirical approaches presented in the thesis entitled "The signed distance
measure in fuzzy statistical analysis. Some theoretical, empirical and
programming advances" (Thesis to be published soon. For the theoretical
approaches, see Berkachy R. and Donze L. (2019)
<doi:10.1007/978-3-030-03368-2_1>. For the empirical approaches, see
Berkachy R. and Donze L. (2016) <ISBN: 978-989-758-201-1>). Important
(non-exhaustive) implementation highlights of this package are as follows:
(1) a numerical procedure to estimate the fuzzy difference and the fuzzy
square. (2) two numerical methods of fuzzification. (3) a function
performing different possibilities of distances, including the signed
distance and the generalized signed distance for instance. (4) numerical
estimations of fuzzy statistical measures such as the variance, the
moment, etc. (5) two methods of estimation of the bootstrap distribution
of the likelihood ratio in the fuzzy context. (6) an estimation of a fuzzy
confidence interval by the likelihood ratio method. (7) testing fuzzy
hypotheses and/or fuzzy data by fuzzy confidence intervals in the
Kwakernaak - Kruse and Meyer sense. (8) a general method to estimate the
fuzzy p-value with fuzzy hypotheses and/or fuzzy data. (9) a method of
estimation of global and individual evaluations of linguistic
questionnaires. (10) numerical estimations of multi-ways analysis of
variance models in the fuzzy context. The unbalance in the considered
designs are also foreseen.

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
