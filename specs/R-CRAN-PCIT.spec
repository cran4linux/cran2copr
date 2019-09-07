%global packname  PCIT
%global packver   1.5-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.3
Release:          1%{?dist}
Summary:          Partial Correlation Coefficient with Information Theory

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10

%description
Apply Partial Correlation coefficient with Information Theory (PCIT) to a
correlation matrix. The PCIT algorithm identifies meaningful correlations
to define edges in a weighted network. The algorithm can be applied to any
correlation-based network including but not limited to gene co-expression
networks. To reduce compute time by making use of multiple compute cores,
simply run PCIT on a computer with has multiple cores and also has the
Rmpi package installed. PCIT will then auto-detect the multicore
environment and run in parallel mode without the need to rewrite your
scripts. This makes scripts, using PCIT, portable across single core (or
no Rmpi package installed) computers which will run in serial mode and
multicore (with Rmpi package installed) computers which will run in
parallel mode.

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
%{rlibdir}/%{packname}/data
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
