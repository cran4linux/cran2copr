%global packname  LongCART
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Recursive Partitioning for Longitudinal Data and Right CensoredData Using Baseline Covariates

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-nlme 
BuildRequires:    R-rpart 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-CRAN-survminer 
BuildRequires:    R-CRAN-Formula 
Requires:         R-nlme 
Requires:         R-rpart 
Requires:         R-survival 
Requires:         R-CRAN-magic 
Requires:         R-CRAN-survminer 
Requires:         R-CRAN-Formula 

%description
Constructs tree for continuous longitudinal data and survival data using
baseline covariates as partitioning variables according to the 'LongCART'
and 'SurvCART' algorithm, respectively.

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
