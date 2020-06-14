%global packname  PROreg
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Patient Reported Outcomes Regression Analysis

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fmsb 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-fmsb 
Requires:         R-CRAN-car 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-numDeriv 
Requires:         R-Matrix 

%description
Offers a variety of tools, such as specific plots and regression model
approaches, for analyzing different patient reported questionnaires.
Specially, mixed-effects models based on the beta-binomial distribution
are implemented to deal with binomial data with over-dispersion (see
Najera-Zuloaga J., Lee D.-J. and Arostegui I. (2017)
<doi:10.1177/0962280217690413>).

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
