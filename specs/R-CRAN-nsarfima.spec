%global packname  nsarfima
%global packver   0.2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0.0
Release:          1%{?dist}
Summary:          Methods for Fitting and Simulating Non-Stationary ARFIMA Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch

%description
Routines for fitting and simulating data under autoregressive fractionally
integrated moving average (ARFIMA) models, without the constraint of
covariance stationarity. Two fitting methods are implemented, a
pseudo-maximum likelihood method and a minimum distance estimator.
Mayoral, L. (2007) <doi:10.1111/j.1368-423X.2007.00202.x>. Beran, J.
(1995) <doi:10.1111/j.2517-6161.1995.tb02054.x>.

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
