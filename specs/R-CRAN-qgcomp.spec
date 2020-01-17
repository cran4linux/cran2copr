%global packname  qgcomp
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}
Summary:          Quantile G-Computation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-arm 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-pscl 
BuildRequires:    R-stats 
BuildRequires:    R-survival 
Requires:         R-CRAN-arm 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-pscl 
Requires:         R-stats 
Requires:         R-survival 

%description
G-computation for a set of time-fixed exposures with quantile-based basis
functions, possibly under linearity and homogeneity assumptions. This
approach estimates a regression line corresponding to the expected change
in the outcome (on the link basis) given a simultaneous increase in the
quantile-based category for all exposures. Works with continuous, binary,
and right-censored time-to-event outcomes.  Reference: Alexander P. Keil,
Jessie P. Buckley, Katie M. OBrien, Kelly K. Ferguson, Shanshan Zhao
Alexandra J. White (2019) A quantile-based g-computation approach to
addressing the effects of exposure mixtures; <arXiv:1902.04200> [stat.ME].

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/fig
%{rlibdir}/%{packname}/INDEX
