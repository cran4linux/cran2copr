%global packname  ompr.roi
%global packver   0.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          3%{?dist}
Summary:          A Solver for 'ompr' that Uses the R Optimization Infrastructure('ROI')

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ompr >= 0.8.0
BuildRequires:    R-CRAN-ROI >= 0.3.0
BuildRequires:    R-CRAN-slam 
BuildRequires:    R-methods 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-ompr >= 0.8.0
Requires:         R-CRAN-ROI >= 0.3.0
Requires:         R-CRAN-slam 
Requires:         R-methods 
Requires:         R-Matrix 

%description
A solver for 'ompr' based on the R Optimization Infrastructure ('ROI').
The package makes all solvers in 'ROI' available to solve 'ompr' models.
Please see the 'ompr' website <https://dirkschumacher.github.io/ompr> and
package docs for more information and examples on how to use it.

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
%{rlibdir}/%{packname}/INDEX
