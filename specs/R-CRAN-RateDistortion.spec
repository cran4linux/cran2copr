%global packname  RateDistortion
%global packver   1.01
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.01
Release:          1%{?dist}
Summary:          Routines for Solving Rate-Distortion Problems

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
An implementation of routines for solving rate-distortion problems.
Rate-distortion theory is a field within information theory that examines
optimal lossy compression. That is, given that some information must be
lost, how can a communication channel be designed that minimizes the cost
of communication error? Rate-distortion theory is concerned with the
optimal (minimal cost) solution to such tradeoffs. An important tool for
solving rate-distortion problems is the Blahut algorithm, developed by
Richard Blahut and described in:

Blahut, R. E. (1972). Computation of channel capacity and rate-distortion
functions. IEEE Transactions on Information Theory, IT-18(4), 460-473.

This package implements the basic Blahut algorithm, and additionally
contains a number of `helper' functions, including a routine for searching
for an information channel that minimizes cost subject to a constraint on
information rate.

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
