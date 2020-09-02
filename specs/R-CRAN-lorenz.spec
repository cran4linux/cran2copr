%global packname  lorenz
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Deriving Income Inequality Estimates from GroupedIncome Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dineq 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dineq 

%description
Provides two methods of estimating income inequality statistics from
binned income data, such as the income data provided in the Census. These
methods use different interpolation techniques to infer the distribution
of incomes within income bins.  One method is an implementation of
Jargowsky and Wheeler's mean-constrained integration over brackets (MCIB).
The other method is based on a new technique, Lorenz interpolation, which
estimates income inequality by constructing an interpolated Lorenz curve
based on the binned income data.  These methods can be used to estimate
three income inequality measures: the Gini (the default measure returned),
the Theil, and the Atkinson's index. Jargowsky and Wheeler (2018)
<doi:10.1177/0081175018782579>.

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
