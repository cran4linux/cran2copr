%global packname  BACCT
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Augmented Control for Clinical Trials

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-rjags 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 

%description
Implements the Bayesian Augmented Control (BAC, a.k.a. Bayesian historical
data borrowing) method under clinical trial setting by calling 'Just
Another Gibbs Sampler' ('JAGS') software. In addition, the 'BACCT' package
evaluates user-specified decision rules by computing the type-I
error/power, or probability of correct go/no-go decision at interim look.
The evaluation can be presented numerically or graphically. Users need to
have 'JAGS' 4.0.0 or newer installed due to a compatibility issue with
'rjags' package. Currently, the package implements the BAC method for
binary outcome only. Support for continuous and survival endpoints will be
added in future releases. We would like to thank AbbVie's Statistical
Innovation group and Clinical Statistics group for their support in
developing the 'BACCT' package.

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
