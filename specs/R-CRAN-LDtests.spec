%global packname  LDtests
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Exact tests for Linkage Disequilibrium and Hardy-Weinberg Equilibrium

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Exact tests for Linkage Disequilibrium (LD) and Hardy-Weinberg Equilibrium
(HWE). - 2-sided LD tests based on different measures of LD (Kulinskaya
and Lewin 2008) - 1-sided Fisher's exact test for LD - 2-sided Haldane
test for HWE (Wiggington 2005) - 1-sided test for inbreeding - conditional
p-values proposed in Kulinskaya (2008) to overcome the problems of
asymetric distributions (for both LD and HWE)

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
