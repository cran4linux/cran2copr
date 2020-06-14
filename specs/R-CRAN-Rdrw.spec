%global packname  Rdrw
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          2%{?dist}
Summary:          Univariate and Multivariate Damped Random Walk Processes

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.2.0
Requires:         R-core >= 2.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm >= 1.0.11
Requires:         R-CRAN-mvtnorm >= 1.0.11

%description
We provide a toolbox to fit and simulate a univariate or multivariate
damped random walk process that is also known as an Ornstein-Uhlenbeck
process or a continuous-time autoregressive model of the first order,
i.e., CAR(1) or CARMA(1, 0). This process is suitable for analyzing
univariate or multivariate time series data with irregularly-spaced
observation times and heteroscedastic measurement errors. When it comes to
the multivariate case, the number of data points
(measurements/observations) available at each observation time does not
need to be the same, and the length of each time series can vary. The
number of time series data sets that can be modeled simultaneously is
limited to ten in this version of the package. We use Kalman-filtering to
evaluate the resulting likelihood function, which leads to a scalable and
efficient computation in finding maximum likelihood estimates of the model
parameters or in drawing their posterior samples. Please pay attention to
loading the data if this package is used for astronomical data analyses;
see the details in the manual. Also see Hu and Tak (2020)
<arXiv:2005.08049>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
