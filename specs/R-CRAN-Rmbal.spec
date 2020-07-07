%global packname  Rmbal
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Estimate Original Hydrocarbon in Place and Reservoir Performance

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-gsl 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-gsl 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-Rdpack 

%description
Material balance analysis for oil and gas reservoirs. Initial hydrocarbon
in place and production forecasts are generated using PVT
(Pressure-Volume-Temperature) and historical injection and production
data. The current version provides history-match and prediction models for
dry-gas, wet-gas, gas condensate, volatile oil, and black oil reservoirs.
Walsh, M. P., Ansah, Joseph, and Raghavan, Rajagopal (1994)
<doi:10.2118/27684-MS>. Walsh, M. P., Ansah, Joseph, and Raghavan,
Rajagopal (1994) <doi:10.2118/27728-MS>. Walsh, M. P. (1995)
<doi:10.2118/95-01-07>.

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
