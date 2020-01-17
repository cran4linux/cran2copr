%global packname  Copula.Markov
%global packver   2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.7
Release:          1%{?dist}
Summary:          Copula-Based Estimation and Statistical Process Control forSerially Correlated Time Series

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Estimation and statistical process control are performed under
copula-based time-series models. Available are statistical methods in Long
and Emura (2014 JCSA), Emura et al. (2017 Commun Stat-Simul)
<DOI:10.1080/03610918.2015.1073303>, Huang and Emura (2019 Commun
Stat-Simul) <DOI:10.1080/03610918.2019.1602647> and Huang, Chen and Emura
(2019-, in revision).

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
