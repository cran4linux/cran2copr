%global packname  monoreg
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          4%{?dist}
Summary:          Bayesian Monotonic Regression Using a Marked Point ProcessConstruction

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gsl-devel
Requires:         gsl
BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0

%description
An extended version of the nonparametric Bayesian monotonic regression
procedure described in Saarela & Arjas (2011)
<DOI:10.1111/j.1467-9469.2010.00716.x>, allowing for multiple additive
monotonic components in the linear predictor, and time-to-event outcomes
through case-base sampling. The extension and its applications, including
estimation of absolute risks, are described in Saarela & Arjas (2015)
<DOI:10.1111/sjos.12125>.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
