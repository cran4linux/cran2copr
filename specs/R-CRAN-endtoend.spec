%global packname  endtoend
%global packver   2.29
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.29
Release:          2%{?dist}
Summary:          Transmissions and Receptions in an End to End Network

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
considering an End-to-End transport model with limited number of
retransmissions per packet. It provides theoretical results and also
estimated values based on Monte Carlo simulations. It is also possible to
consider random data and ACK probabilities.

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
