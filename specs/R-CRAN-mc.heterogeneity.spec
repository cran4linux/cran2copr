%global packname  mc.heterogeneity
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          A Monte Carlo Based Heterogeneity Test for Meta-Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-CRAN-metafor 
Requires:         R-utils 

%description
Implements a Monte Carlo Based Heterogeneity Test for standardized mean
differences (d), Fisher-transformed Pearson's correlations (r), and
natural-logarithm-transformed odds ratio (OR) in Meta-Analysis Studies.
Depending on the presence of moderators, this Monte Carlo Based Test can
be implemented in the random or mixed-effects model. This package uses
rma() function from the R package 'metafor' to obtain parameter estimates
and likelihood, so installation of R package 'metafor' is required.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
