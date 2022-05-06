%global __brp_check_rpaths %{nil}
%global packname  diffcor
%global packver   0.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fisher's z-Tests Concerning Difference of Correlations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Computations of Fisher's z-tests concerning differences between
correlations. diffcor.one() can be used to test whether an expected value
differs from an observed value, for example, in construct validation.
diffcor.two() can be used to test if the correlation between two
constructs differed between two studies. diffcor.dep() can be applied to
check if the correlation between two constructs (r12) is significantly
different from the correlation of the first construct with a third one
(r13), given the intercorrelation of the compared constructs (r23). All
outputs provide the compared correlations, test statistic in z-units, and
p-values. For diffcor.one() and diffcor.two(), the output further provides
confidence intervals of the empirical correlations and the effect size
Cohens q. According to Cohen (1988), q = |.10|, |.30| and |.50| are
considered small, moderate, and large differences, respectively.

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
