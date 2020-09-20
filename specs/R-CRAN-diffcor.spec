%global packname  diffcor
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
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
correlations. diffcor.one() could be used to test for differences
regarding an expected value, e.g., in construct validation. diffcor.two()
may be useful in replication studies, to test if the original study and
the replication study differed in terms of effects. diffcor.dep() can be
applied to check if the correlation between one construct with another one
(r12) is significantly different/higher/smaller than the correlation of
one of the constructs with a third construct (r13), given the correlation
of the constructs that are compared (r23). The outputs for all the three
functions provide the test statistic in z-units as well as p-values. For
diffcor.one() and diffcor.two(), the effect size Cohens q is additionally
printed. It is a descriptive index to evaluate differences of independent
correlations. Cohen (1988) suggested q = |.10|, |.30| and |.50| as small,
moderate, and large differences.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
