%global __brp_check_rpaths %{nil}
%global packname  metaRMST
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Meta-Analysis of RMSTD

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rstpm2 
BuildRequires:    R-CRAN-mvmeta 
BuildRequires:    R-CRAN-meta 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-survRM2 
BuildRequires:    R-graphics 
Requires:         R-CRAN-rstpm2 
Requires:         R-CRAN-mvmeta 
Requires:         R-CRAN-meta 
Requires:         R-survival 
Requires:         R-CRAN-survRM2 
Requires:         R-graphics 

%description
R implementation of a multivariate meta-analysis of randomized controlled
trials (RCT) with the difference in restricted mean survival times
(RMSTD). Use this package with individual patient level data from an RCT
for a time-to-event outcome to determine combined effect estimates
according to 4 methods: 1) a univariate meta-analysis using observed
treatment effects, 2) a univariate meta-analysis using effects predicted
by fitted Royston-Parmar flexible parametric models, 3) multivariate
meta-analysis with analytically derived covariance, 4) multivariate
meta-analysis with bootstrap derived covariance. This package computes all
combined effects and provides an RMSTD curve with combined effect
estimates and their confidence intervals.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
