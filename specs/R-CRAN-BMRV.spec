%global packname  BMRV
%global packver   1.32
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.32
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Models for Rare Variant Association Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-BH 
Requires:         R-stats 

%description
Provides two Bayesian models for detecting the association between rare
genetic variants and a trait that can be continuous, ordinal or binary.
Bayesian latent variable collapsing model (BLVCM) detects interaction
effect and is dedicated to twin design while it can also be applied to
independent samples. Hierarchical Bayesian multiple regression model
(HBMR) incorporates genotype uncertainty information and can be applied to
either independent or family samples. Furthermore, it deals with
continuous, binary and ordinal traits.

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
%{rlibdir}/%{packname}/libs
