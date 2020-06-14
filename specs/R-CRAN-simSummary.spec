%global packname  simSummary
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Simulation summary

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-gdata >= 2.8.0
BuildRequires:    R-CRAN-abind >= 1.4.0
BuildRequires:    R-CRAN-svUnit >= 0.7.5
Requires:         R-CRAN-gdata >= 2.8.0
Requires:         R-CRAN-abind >= 1.4.0
Requires:         R-CRAN-svUnit >= 0.7.5

%description
simSummary is a small utility package which eases the process of
summarizing simulation results. Simulations often produce intermediate
results - some focal statistics that need to be summarized over several
scenarios and many replications. This step is in principle easy, but
tedious. The package simSummary fills this niche by providing a generic
way of summarizing the focal statistics of simulations. The useR must
provide properly structured input, holding focal statistics, and then the
summary step can be performed with one line of code, calling the
simSummary function.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/INDEX
