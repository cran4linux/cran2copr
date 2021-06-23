%global __brp_check_rpaths %{nil}
%global packname  SBAGM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Search Best ARIMA, GARCH, and MS-GARCH Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-MSGARCH 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-rugarch 
Requires:         R-CRAN-MSGARCH 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-rugarch 

%description
Get the most appropriate autoregressive integrated moving average,
generalized auto-regressive conditional heteroscedasticity and Markov
switching GARCH model. For method details see Haas M, Mittnik S, Paolella
MS (2004). <doi:10.1093/jjfinec/nbh020>, Bollerslev T (1986).
<doi:10.1016/0304-4076(86)90063-1>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
