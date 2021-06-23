%global __brp_check_rpaths %{nil}
%global packname  memochange
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Testing for Structural Breaks under Long Memory and Testing forChanges in Persistence

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast >= 8.6
BuildRequires:    R-stats >= 3.4.1
BuildRequires:    R-CRAN-sandwich >= 2.5.1
BuildRequires:    R-CRAN-strucchange >= 1.5.1
BuildRequires:    R-CRAN-fracdiff >= 1.4.2
BuildRequires:    R-CRAN-urca >= 1.3.0
BuildRequires:    R-CRAN-longmemo >= 1.1.1
BuildRequires:    R-CRAN-LongMemoryTS >= 0.1.0
Requires:         R-CRAN-forecast >= 8.6
Requires:         R-stats >= 3.4.1
Requires:         R-CRAN-sandwich >= 2.5.1
Requires:         R-CRAN-strucchange >= 1.5.1
Requires:         R-CRAN-fracdiff >= 1.4.2
Requires:         R-CRAN-urca >= 1.3.0
Requires:         R-CRAN-longmemo >= 1.1.1
Requires:         R-CRAN-LongMemoryTS >= 0.1.0

%description
Test procedures and break point estimators for persistent processes that
exhibit structural breaks in mean or in persistence. On the one hand the
package contains the most popular approaches for testing whether a time
series exhibits a break in persistence from I(0) to I(1) or vice versa,
such as those of Busetti and Taylor (2004) and Leybourne, Kim, and Taylor
(2007). The approach by Martins and Rodrigues (2014), which allows to
detect changes from I(d1) to I(d2) with d1 and d2 being non-integers, is
included as well. In case the tests reject the null of constant
persistence, various breakpoint estimators are available to detect the
point of the break as well as the order of integration in the two regimes.
On the other hand the package contains the most popular approaches to test
for a change-in-mean of a long-memory time series, which were recently
reviewed by Wenger, Leschinski, and Sibbertsen (2018). These include
memory robust versions of the CUSUM, sup-Wald, and Wilcoxon type tests.
The tests either utilize consistent estimates of the long-run variance or
a self normalization approach in their test statistics. Betken (2016)
<doi:10.1111/jtsa.12187> Busetti and Taylor (2004)
<doi:10.1016/j.jeconom.2003.10.028> Dehling, Rooch and Taqqu (2012)
<doi:10.1111/j.1467-9469.2012.00799.x> Harvey, Leybourne and Taylor (2006)
<doi:10.1016/j.jeconom.2005.07.002> Horvath and Kokoszka (1997)
<doi:10.1016/S0378-3758(96)00208-X> Hualde and Iacone (2017)
<doi:10.1016/j.econlet.2016.10.014> Iacone, Leybourne and Taylor (2014)
<doi:10.1111/jtsa.12049> Leybourne, Kim, Smith, and Newbold (2003)
<doi:10.1111/1368-423X.t01-1-00110> Leybourne and Taylor (2004)
<doi:10.1016/j.econlet.2003.12.015> Leybourne, Kim, and Taylor (2007):
<doi:10.1111/j.1467-9892.2006.00517.x> Martins and Rodrigues (2014)
<doi:10.1016/j.csda.2012.07.021> Shao (2011)
<doi:10.1111/j.1467-9892.2010.00717.x> Sibbertsen and Kruse (2009)
<doi:10.1111/j.1467-9892.2009.00611.x> Wang (2008)
<doi:10.1080/00949650701216604> Wenger, Leschinski and Sibbertsen (2018)
<doi:10.1016/j.econlet.2017.12.007>.

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
