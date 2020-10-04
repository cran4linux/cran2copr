%global packname  GSED
%global packver   2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5
Release:          3%{?dist}%{?buildtag}
Summary:          Group Sequential Enrichment Design

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-survival >= 2.37.7
BuildRequires:    R-CRAN-R.utils >= 2.3.0
BuildRequires:    R-CRAN-rootSolve >= 1.6.6
BuildRequires:    R-CRAN-memoise >= 1.0.0
Requires:         R-survival >= 2.37.7
Requires:         R-CRAN-R.utils >= 2.3.0
Requires:         R-CRAN-rootSolve >= 1.6.6
Requires:         R-CRAN-memoise >= 1.0.0

%description
Provides function to apply "Group sequential enrichment design
incorporating subgroup selection" (GSED) method proposed by Magnusson and
Turnbull (2013) <doi:10.1002/sim.5738>.

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
