%global packname  pairwiseCI
%global packver   0.1-27
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.27
Release:          3%{?dist}
Summary:          Confidence Intervals for Two Sample Comparisons

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-coin >= 1.3.0
BuildRequires:    R-CRAN-MCPAN 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-boot 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mcprofile 
Requires:         R-CRAN-coin >= 1.3.0
Requires:         R-CRAN-MCPAN 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-boot 
Requires:         R-MASS 
Requires:         R-CRAN-mcprofile 

%description
Calculation of the parametric, nonparametric confidence intervals for the
difference or ratio of location parameters, nonparametric confidence
interval for the Behrens-Fisher problem and for the difference, ratio and
odds-ratio of binomial proportions for comparison of independent samples.
Common wrapper functions to split data sets and apply confidence intervals
or tests to these subsets. A by-statement allows calculation of CI
separately for the levels of further factors. CI are not adjusted for
multiplicity.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
