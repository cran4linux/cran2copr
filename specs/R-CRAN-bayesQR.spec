%global packname  bayesQR
%global packver   2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3
Release:          3%{?dist}
Summary:          Bayesian Quantile Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildRequires:    R-graphics >= 3.0
BuildRequires:    R-methods >= 3.0
BuildRequires:    R-stats >= 3.0
BuildRequires:    R-utils >= 2.0
Requires:         R-graphics >= 3.0
Requires:         R-methods >= 3.0
Requires:         R-stats >= 3.0
Requires:         R-utils >= 2.0

%description
Bayesian quantile regression using the asymmetric Laplace distribution,
both continuous as well as binary dependent variables are supported. The
package consists of implementations of the methods of Yu & Moyeed (2001)
<doi:10.1016/S0167-7152(01)00124-9>, Benoit & Van den Poel (2012)
<doi:10.1002/jae.1216> and Al-Hamzawi, Yu & Benoit (2012)
<doi:10.1177/1471082X1101200304>. To speed up the calculations, the Markov
Chain Monte Carlo core of all algorithms is programmed in Fortran and
called from R.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
