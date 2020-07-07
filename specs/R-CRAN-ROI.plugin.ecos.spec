%global packname  ROI.plugin.ecos
%global packver   0.3-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          3%{?dist}
Summary:          'ECOS' Plugin for the 'R' Optimization Infrastructure

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ECOSolveR >= 0.3.1
BuildRequires:    R-CRAN-ROI >= 0.3.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-slam 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-ECOSolveR >= 0.3.1
Requires:         R-CRAN-ROI >= 0.3.0
Requires:         R-methods 
Requires:         R-CRAN-slam 
Requires:         R-Matrix 

%description
Enhances the 'R' Optimization Infrastructure ('ROI') package with the
Embedded Conic Solver ('ECOS') for solving conic optimization problems.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
