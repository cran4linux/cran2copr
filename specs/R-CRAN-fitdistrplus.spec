%global packname  fitdistrplus
%global packver   1.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          3%{?dist}
Summary:          Help to Fit of a Parametric Distribution to Non-Censored orCensored Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-grDevices 
BuildRequires:    R-survival 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-MASS 
Requires:         R-grDevices 
Requires:         R-survival 
Requires:         R-methods 
Requires:         R-stats 

%description
Extends the fitdistr() function (of the MASS package) with several
functions to help the fit of a parametric distribution to non-censored or
censored data. Censored data may contain left censored, right censored and
interval censored values, with several lower and upper bounds. In addition
to maximum likelihood estimation (MLE), the package provides moment
matching (MME), quantile matching (QME) and maximum goodness-of-fit
estimation (MGE) methods (available only for non-censored data). Weighted
versions of MLE, MME and QME are available. See e.g. Casella & Berger
(2002). Statistical inference. Pacific Grove.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
