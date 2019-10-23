%global packname  Density.T.HoldOut
%global packver   2.00
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.00
Release:          1%{?dist}
Summary:          Density.T.HoldOut: Non-combinatorial T-estimation Hold-Out fordensity estimation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-histogram 
Requires:         R-CRAN-histogram 

%description
Implementation in the density framework of the non-combinatorial algorithm
and its greedy version, introduced by Magalhães and Rozenholc (2014), for
T-estimation Hold-Out proposed in Birgé (2006, Section 9). The package
provide an implementation which uses several families of estimators
(regular and irregular histograms, kernel estimators) which may be used
alone or combined. As a complement, provides also a comparison with other
Held-Out derived from least-squares and maximum-likelihood. This package
implements also the T-estimation Hold-Out derived from the test introduced
in Baraud (2011).

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
