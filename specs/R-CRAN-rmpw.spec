%global packname  rmpw
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          2%{?dist}
Summary:          Causal Mediation Analysis Using Weighting Approach

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-MASS 
Requires:         R-CRAN-gtools 
Requires:         R-MASS 

%description
We implement causal mediation analysis using the methods proposed by Hong
(2010) and Hong, Deutsch & Hill (2015) <doi:10.3102/1076998615583902>. It
allows the estimation and hypothesis testing of causal mediation effects
through ratio of mediator probability weights (RMPW). This strategy
conveniently relaxes the assumption of no treatment-by-mediator
interaction while greatly simplifying the outcome model specification
without invoking strong distributional assumptions. We also implement a
sensitivity analysis by extending the RMPW method to assess potential bias
in the presence of omitted pretreatment or posttreatment covariates. The
sensitivity analysis strategy was proposed by Hong, Qin, and Yang (2018)
<doi:10.3102/1076998617749561>.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
