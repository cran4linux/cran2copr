%global packname  betareg
%global packver   3.1-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Beta Regression

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-flexmix 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-modeltools 
BuildRequires:    R-CRAN-sandwich 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-flexmix 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-modeltools 
Requires:         R-CRAN-sandwich 

%description
Beta regression for modeling beta-distributed dependent variables, e.g.,
rates and proportions. In addition to maximum likelihood regression (for
both mean and precision of a beta-distributed response), bias-corrected
and bias-reduced estimation as well as finite mixture models and recursive
partitioning for beta regressions are provided.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
