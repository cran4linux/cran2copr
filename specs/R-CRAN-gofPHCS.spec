%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gofPHCS
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Goodness-of-Fit Tests for Complete, Progressively Type-II, Type-I Hybrid, and Type-II Hybrid Censored Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-withr 
Requires:         R-stats 
Requires:         R-CRAN-withr 

%description
Provides goodness-of-fit tests for lifetime data collected under complete
sampling, progressive Type-II censoring, and Type-I/Type-II hybrid
censoring schemes. Users supply the observed (censored) data and the
assumed probability density/mass function, cumulative distribution
function, or survival function of the target model, and the package
returns the corresponding test statistic together with an asymptotic or
Monte Carlo p-value. Implements the spacings-based exponentiality test of
Balakrishnan, Ng and Kannan (2002, in "Goodness-of-Fit Tests and Model
Validity", Birkhauser, pp. 89-111) and its location-scale generalization
Balakrishnan, Ng and Kannan (2004) <doi:10.1109/TR.2004.833317>, the power
comparison and Kaplan-Meier based tests of Doering and Cramer (2019)
<doi:10.1080/00949655.2019.1648468>, the Kolmogorov-Smirnov type tests for
hybrid censored data of Banerjee and Pradhan (2018)
<doi:10.1080/03610926.2016.1205616>, and follows the unified treatment of
hybrid censoring schemes reviewed in Balakrishnan and Kundu (2013)
<doi:10.1016/j.csda.2012.03.025> and in Cramer and Balakrishnan (2023,
"Hybrid Censoring Know-How", Chapter 11)
<doi:10.1016/B978-0-12-398387-9.00019-2>.

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
