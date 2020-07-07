%global packname  supportInt
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}
Summary:          Calculates Likelihood Support Intervals for Common Data Types

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ProfileLikelihood 
BuildRequires:    R-splines 
Requires:         R-CRAN-ProfileLikelihood 
Requires:         R-splines 

%description
Calculates likelihood based support intervals for several common data
types including binomial, Poisson, normal, lm(), and glm(). For the
binomial, Poisson, and normal data likelihood intervals are calculated via
root finding algorithm. Additional parameters allow the user to specify
whether they would like to receive a parametric bootstrap estimate of the
confidence level of said support interval. For lm() and glm(), the
function returns profile likelihoods for each coefficient in the model.

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
