%global packname  selectiongain
%global packver   2.0.591
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.591
Release:          3%{?dist}%{?buildtag}
Summary:          A Tool for Calculation and Optimization of the Expected Gainfrom Multi-Stage Selection

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-parallel 
Requires:         R-CRAN-mvtnorm 
Requires:         R-parallel 

%description
Multi-stage selection is practiced in numerous fields of life and social
sciences and particularly in breeding. A special characteristic of
multi-stage selection is that candidates are evaluated in successive
stages with increasing intensity and effort, and only a fraction of the
superior candidates is selected and promoted to the next stage. For the
optimum design of such selection programs, the selection gain plays a
crucial role. It can be calculated by integration of a truncated
multivariate normal (MVN) distribution. While mathematical formulas for
calculating the selection gain and the variance among selected candidates
were developed long time ago, solutions for numerical calculation were not
available. This package can also be used for optimizing multi-stage
selection programs for a given total budget and different costs of
evaluating the candidates in each stage.

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
