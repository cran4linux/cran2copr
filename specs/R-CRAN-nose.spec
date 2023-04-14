%global __brp_check_rpaths %{nil}
%global packname  nose
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          nose Package for R

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
The nose package consists of a collection of three functions for
classifying sparseness in typical 2 x 2 data sets with at least one cell
should have zero count. These functions are based on the three widely
applied summary measures for 2 x 2 categorical data viz, Risk Difference
(RD), Relative Risk (RR), Odds Ratio (OR). This package helps to identify
suitable continuity correction for zero cells when a multi centre analysis
or a meta analysis is carried out. Further, it can be considered as a tool
for sensitivity analysis for adding a continuity correction and to
identify the presence of Simpson's paradox.

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
