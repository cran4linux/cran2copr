%global packname  not
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}
Summary:          Narrowest-Over-Threshold Change-Point Detection

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-splines 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-splines 

%description
Provides efficient implementation of the Narrowest-Over-Threshold
methodology for detecting an unknown number of change-points occurring at
unknown locations in one-dimensional data following deterministic signal +
noise model, see R. Baranowski, Y. Chen and P. Fryzlewicz (2019)
<doi:10.1111/rssb.12322>. Currently implemented scenarios are:
piecewise-constant signal, piecewise-constant signal with a heavy-tailed
noise, piecewise-linear signal, piecewise-quadratic signal,
piecewise-constant signal and with piecewise-constant variance of the
noise.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
