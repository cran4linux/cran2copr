%global __brp_check_rpaths %{nil}
%global packname  corTest
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Tests for Equal Correlation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-MASS 
Requires:         R-graphics 
Requires:         R-stats 

%description
There are 6 novel robust tests for equal correlation. They are all based
on logistic regressions. The score statistic U is proportion to difference
of two correlations based on different types of correlation in 6 methods.
The ST1() is based on Pearson correlation. ST2() improved ST1() by using
median absolute deviation. ST3() utilized type M correlation and ST4()
used Spearman correlation.  ST5() and ST6() used two different ways to
combine ST3() and ST4().  We highly recommend ST5() according to the
article titled ''New Statistical Methods for Constructing Robust
Differential Correlation Networks to characterize the interactions among
microRNAs'' published in Scientific Reports.  Please see the reference: Yu
et al. (2019) <doi:10.1038/s41598-019-40167-8>.

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
