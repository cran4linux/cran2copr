%global __brp_check_rpaths %{nil}
%global packname  moezipfR
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Marshall-Olkin Extended Zipf

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0.1
Requires:         R-core >= 2.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-tolerance >= 1.2.0
BuildRequires:    R-CRAN-VGAM >= 0.9.8
Requires:         R-CRAN-tolerance >= 1.2.0
Requires:         R-CRAN-VGAM >= 0.9.8

%description
Statistical utilities for the analysis of data by means of the
Marshall-Olkin Extended Zipf distribution are presented. The distribution
is a two-parameter extension of the widely used Zipf model. By plotting
the probabilities in log-log scale, this two-parameter extension allows a
concave as well as a convex behavior of the function at the beginning of
the distribution, maintaining the linearity, associated to the Zipf model,
in the tail.

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
