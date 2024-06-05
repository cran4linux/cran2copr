%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RARtrials
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Response-Adaptive Randomization in Clinical Trials

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3
Requires:         R-core >= 4.3
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack >= 0.7
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pins 
Requires:         R-CRAN-Rdpack >= 0.7
Requires:         R-stats 
Requires:         R-CRAN-pins 

%description
Some response-adaptive randomization methods commonly found in literature
are included in this package. These methods include the randomized
play-the-winner rule for binary endpoint (Wei and Durham (1978)
<doi:10.2307/2286290>), the doubly adaptive biased coin design with
minimal variance strategy for binary endpoint (Atkinson and Biswas (2013)
<doi:10.1201/b16101>, Rosenberger and Lachin (2015)
<doi:10.1002/9781118742112>) and maximal power strategy targeting Neyman
allocation for binary endpoint (Tymofyeyev, Rosenberger, and Hu (2007)
<doi:10.1198/016214506000000906>) and RSIHR allocation with each letter
representing the first character of the names of the individuals who first
proposed this rule (Youngsook and Hu (2010) <doi:10.1198/sbr.2009.0056>,
Bello and Sabo (2016) <doi:10.1080/00949655.2015.1114116>), A-optimal
Allocation for continuous endpoint (Sverdlov and Rosenberger (2013)
<doi:10.1080/15598608.2013.783726>), Aa-optimal Allocation for continuous
endpoint (Sverdlov and Rosenberger (2013)
<doi:10.1080/15598608.2013.783726>), generalized RSIHR allocation for
continuous endpoint (Atkinson and Biswas (2013) <doi:10.1201/b16101>),
Bayesian response-adaptive randomization with a control group using the
Thall & Wathen method for binary and continuous endpoints (Thall and
Wathen (2007) <doi:10.1016/j.ejca.2007.01.006>) and the forward-looking
Gittins index rule for binary and continuous endpoints (Villar, Wason, and
Bowden (2015) <doi:10.1111/biom.12337>, Williamson and Villar (2019)
<doi:10.1111/biom.13119>).

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
