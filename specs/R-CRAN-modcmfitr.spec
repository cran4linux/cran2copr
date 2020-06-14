%global packname  modcmfitr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Fit a Modified Connor-Mosimann Distribution to ElicitedQuantiles in Multinomial Problems

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.2
Requires:         R-core >= 3.4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-gtools >= 3.5.0
BuildRequires:    R-CRAN-nloptr >= 1.0.4
Requires:         R-CRAN-gtools >= 3.5.0
Requires:         R-CRAN-nloptr >= 1.0.4

%description
Fits a modified version of the Connor-Mosimann distribution (Connor &
Mosimann (1969)<doi:10.2307/2283728>), a Connor-Mosimann distribution or
Dirichlet distribution (e.g. Gelman, Carlin, Stern & Rubin Chapter 3.5
(2004, <ISBN:1-58488-388-X>) to elicited quantiles of a multinomial
distribution. Code is also provided to sample from the distributions,
generating inputs suitable for a probabilistic sensitivity analysis /
Monte Carlo simulation in a decision model.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
