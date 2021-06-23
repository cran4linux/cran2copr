%global __brp_check_rpaths %{nil}
%global packname  easyDes
%global packver   5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.0
Release:          3%{?dist}%{?buildtag}
Summary:          An Easy Way to Descriptive Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-PMCMRplus 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-PMCMRplus 
Requires:         R-CRAN-multcomp 
Requires:         R-stats 
Requires:         R-utils 

%description
Descriptive analysis is essential for publishing medical articles. This
package provides an easy way to conduct the descriptive analysis. 1. Both
numeric and factor variables can be handled. For numeric variables,
normality test will be applied to choose the parametric and nonparametric
test. 2. Both two or more groups can be handled. For groups more than two,
the post hoc test will be applied, 'Tukey' for the numeric variables and
'FDR' for the factor variables. 3. T test, ANOVA or Fisher test can be
forced to apply. 4. Mean and standard deviation can be forced to display.

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
