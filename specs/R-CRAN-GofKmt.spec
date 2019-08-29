%global packname  GofKmt
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}
Summary:          Khmaladze Martingale Transformation Goodness-of-Fit Test

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-Rsolnp 
Requires:         R-CRAN-Rsolnp 

%description
Consider a goodness-of-fit(GOF) problem of testing whether a random sample
comes from one sample location-scale model where location and scale
parameters are unknown. It is well known that Khmaladze martingale
transformation method provides asymptotic distribution free test for the
GOF problem. This package contains one function: KhmaladzeTrans(). In this
version, KhmaladzeTrans() provides test statistic and critical value of
GOF test for normal, Cauchy, logistic, Gamma, Weibull, Gumbel, and
Rayleigh distributions.

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
