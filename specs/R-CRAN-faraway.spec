%global packname  faraway
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          3%{?dist}%{?buildtag}
Summary:          Functions and Datasets for Books by Julian Faraway

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-nlme 
BuildRequires:    R-methods 
Requires:         R-CRAN-lme4 
Requires:         R-nlme 
Requires:         R-methods 

%description
Books are "Practical Regression and ANOVA in R" on CRAN, "Linear Models
with R" published 1st Ed. August 2004, 2nd Ed. July 2014 by CRC press,
ISBN 9781439887332, and "Extending the Linear Model with R" published by
CRC press in 1st Ed. December 2005 and 2nd Ed. March 2016, ISBN
9781584884248.

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
