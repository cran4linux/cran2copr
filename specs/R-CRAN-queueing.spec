%global packname  queueing
%global packver   0.2.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.11
Release:          1%{?dist}
Summary:          Analysis of Queueing Networks and Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 2.11.1
Requires:         R-core >= 2.11.1
BuildArch:        noarch

%description
It provides versatile tools for analysis of birth and death based
Markovian Queueing Models and Single and Multiclass Product-Form Queueing
Networks. It implements M/M/1, M/M/c, M/M/Infinite, M/M/1/K, M/M/c/K,
M/M/c/c, M/M/1/K/K, M/M/c/K/K, M/M/c/K/m, M/M/Infinite/K/K, Multiple
Channel Open Jackson Networks, Multiple Channel Closed Jackson Networks,
Single Channel Multiple Class Open Networks, Single Channel Multiple Class
Closed Networks and Single Channel Multiple Class Mixed Networks. Also it
provides a B-Erlang, C-Erlang and Engset calculators. This work is
dedicated to the memory of D. Sixto Rios Insua.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
