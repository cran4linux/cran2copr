%global packname  BetaPASS
%global packver   1.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Calculate Power and Sample Size with Beta Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-betareg 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-stats 
Requires:         R-CRAN-betareg 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-pbapply 
Requires:         R-stats 

%description
Power calculations are a critical component of any research study to
determine the minimum sample size necessary to detect differences between
multiple groups. Researchers often work with data taking the form of
proportions that can be modeled with a beta distribution. Here we present
an R package, 'BetaPASS', that perform power and sample size calculations
for data following a beta distribution with comparative nonparametric
output. This package allows flexibility with multiple options for link
functions to fit the data and graphing functionality for visual
comparisons.

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
