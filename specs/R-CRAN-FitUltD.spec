%global packname  FitUltD
%global packver   3.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Fit Univariate Mixed and Usual Distributions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-ADGofTest 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-ADGofTest 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-assertthat 
Requires:         R-MASS 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-cowplot 
Requires:         R-methods 
Requires:         R-stats 

%description
Extends the fitdist() (from 'fitdistrplus') adding the Anderson-Darling
ad.test() (from 'ADGofTest') and Kolmogorov Smirnov Test ks.test() inside,
trying the distributions from 'stats' package by default and offering a
second function which uses mixed distributions to fit, this distributions
are split with unsupervised learning, with Mclust() function (from
'mclust').

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
