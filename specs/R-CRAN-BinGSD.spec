%global packname  BinGSD
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Calculation for Single Arm Group Sequential Test with BinaryEndpoint

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods >= 3.5.0
BuildRequires:    R-stats >= 3.5.0
BuildRequires:    R-CRAN-mvtnorm >= 1.0.11
Requires:         R-methods >= 3.5.0
Requires:         R-stats >= 3.5.0
Requires:         R-CRAN-mvtnorm >= 1.0.11

%description
Consider an at-most-K-stage group sequential design with only an upper
bound for the last analysis and non-binding lower bounds.With binary
endpoint, two kinds of test can be applied, asymptotic test based on
normal distribution and exact test based on binomial distribution. This
package supports the computation of boundaries and conditional power for
single-arm group sequential test with binary endpoint, via either
asymptotic or exact test. The package also provides functions to obtain
boundary crossing probabilities given the design.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/docs
%{rlibdir}/%{packname}/INDEX
