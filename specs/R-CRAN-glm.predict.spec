%global packname  glm.predict
%global packver   3.1-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.0
Release:          1%{?dist}
Summary:          Predicted Values and Discrete Changes for GLM

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
BuildRequires:    R-parallel 
BuildRequires:    R-nnet 
Requires:         R-stats 
Requires:         R-MASS 
Requires:         R-parallel 
Requires:         R-nnet 

%description
Functions to calculate predicted values and the difference between the two
cases with confidence interval for lm() [linear model], glm() [general
linear model], glm.nb() [negative binomial model], polr() [ordinal
logistic model] and multinom() [multinomial model] using Monte Carlo
simulations. Reference: Bennet A. Zelner (2009) <doi:10.1002/smj.783>.

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
