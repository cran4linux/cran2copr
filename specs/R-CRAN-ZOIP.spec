%global packname  ZOIP
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          2%{?dist}
Summary:          ZOIP Distribution, ZOIP Regression, ZOIP Mixed Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rmutil 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-GHQp 
BuildRequires:    R-stats 
Requires:         R-CRAN-rmutil 
Requires:         R-boot 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-GHQp 
Requires:         R-stats 

%description
The ZOIP distribution (Zeros Ones Inflated Proportional) is a proportional
data distribution inflated with zeros and/or ones, this distribution is
defined on the most known proportional data distributions, the beta and
simplex distribution, Jørgensen and Barndorff-Nielsen (1991)
<doi:10.1016/0047-259X(91)90008-P>, also allows it to have different
parameterizations of the beta distribution, Ferrari and Cribari-Neto
(2004) <doi:10.1080/0266476042000214501>, Rigby and Stasinopoulos (2005)
<doi:10.18637/jss.v023.i07>. The ZOIP distribution has four parameters,
two of which correspond to the proportion of zeros and ones, and the other
two correspond to the distribution of the proportional data of your
choice. The 'ZOIP' package allows adjustments of regression models for
fixed and mixed effects for proportional data inflated with zeros and/or
ones.

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
