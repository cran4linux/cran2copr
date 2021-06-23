%global __brp_check_rpaths %{nil}
%global packname  Exact
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Unconditional Exact Test

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rootSolve 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-rootSolve 

%description
Performs unconditional exact tests and power calculations for 2x2
contingency tables.  Calculates Barnard's test (1945)
<doi:10.1038/156177a0> using the original CSM test (Barnard, 1947
<doi:10.1093/biomet/34.1-2.123>), using Fisher's p-value referred to as
Boschloo's test (1970) <doi:10.1111/j.1467-9574.1970.tb00104.x>, or using
a Z-statistic (Suissa and Shuster, 1985, <doi:10.2307/2981892>).
Calculations confidence intervals for the difference in proportion.

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
