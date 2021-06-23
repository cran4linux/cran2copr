%global __brp_check_rpaths %{nil}
%global packname  estimraw
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of Four-Fold Table Cell Frequencies (Raw Data) fromEffect Size Measures

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-dplyr 

%description
Estimation of four-fold table cell frequencies (raw data) from risk ratios
(relative risks), risk differences and odds ratios. While raw data can be
useful for doing meta-analysis, such data is often not provided by primary
studies (with summary statistics being solely presented). Therefore, based
on summary statistics (namely, risk ratios, risk differences and odds
ratios), this package estimates the value of each cell in a 2x2 table
according to the equations described in Di Pietrantonj C (2006)
<doi:10.1002/sim.2287>.

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
