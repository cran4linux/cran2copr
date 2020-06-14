%global packname  SmithWilsonYieldCurve
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          2%{?dist}
Summary:          Smith-Wilson Yield Curve Construction

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Constructs a yield curve by the Smith-Wilson method from a table of LIBOR
and SWAP rates

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
%doc %{rlibdir}/%{packname}/figure
%doc %{rlibdir}/%{packname}/InstrumentSet.csv
%doc %{rlibdir}/%{packname}/SmithWilsonMethod.html
%doc %{rlibdir}/%{packname}/SmithWilsonMethod.md
%doc %{rlibdir}/%{packname}/SmithWilsonMethod.Rmd
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
