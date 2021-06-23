%global __brp_check_rpaths %{nil}
%global packname  dfmta
%global packver   1.7-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.1
Release:          3%{?dist}%{?buildtag}
Summary:          Phase I/II Adaptive Dose-Finding Design for MTA

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-BH >= 1.55
BuildRequires:    R-CRAN-RcppArmadillo >= 0.7.100.3.1
BuildRequires:    R-CRAN-RcppProgress >= 0.2.1
BuildRequires:    R-CRAN-Rcpp 

%description
Phase I/II adaptive dose-finding design for single-agent Molecularly
Targeted Agent (MTA), according to the paper "Phase I/II Dose-Finding
Design for Molecularly Targeted Agent: Plateau Determination using
Adaptive Randomization", Riviere Marie-Karelle et al. (2016)
<doi:10.1177/0962280216631763>.

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
