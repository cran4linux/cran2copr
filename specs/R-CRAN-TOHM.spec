%global packname  TOHM
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          2%{?dist}
Summary:          Testing One Hypothesis Multiple Times

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-Rmpfr 
BuildRequires:    R-CRAN-EQL 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-igraph 
Requires:         R-Matrix 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-Rmpfr 
Requires:         R-CRAN-EQL 
Requires:         R-methods 
Requires:         R-stats 

%description
Approximations of global p-values when testing hypothesis in presence of
non-identifiable nuisance parameters. The method relies on the Euler
characteristic heuristic and the expected Euler characteristic is
efficiently computed by in Algeri and van Dyk (2018) <arXiv:1803.03858>.

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
