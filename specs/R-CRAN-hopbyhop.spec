%global __brp_check_rpaths %{nil}
%global packname  hopbyhop
%global packver   3.41
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.41
Release:          3%{?dist}%{?buildtag}
Summary:          Transmissions and Receptions in a Hop by Hop Network

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-pastecs 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-pastecs 
Requires:         R-CRAN-ggplot2 

%description
Computes the expectation of the number of transmissions and receptions
considering a Hop-by-Hop transport model with limited number of
retransmissions per packet. It provides the theoretical results shown in
Palma et. al.(2016) <DOI:10.1109/TLA.2016.7555237> and also estimated
values based on Monte Carlo simulations. It is also possible to consider
random data and ACK probabilities.

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
