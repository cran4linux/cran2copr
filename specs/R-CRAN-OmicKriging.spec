%global packname  OmicKriging
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          3%{?dist}
Summary:          Poly-Omic Prediction of Complex TRaits

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildArch:        noarch
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-ROCR 
Requires:         R-CRAN-irlba 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 

%description
It provides functions to generate a correlation matrix from a genetic
dataset and to use this matrix to predict the phenotype of an individual
by using the phenotypes of the remaining individuals through kriging.
Kriging is a geostatistical method for optimal prediction or best unbiased
linear prediction. It consists of predicting the value of a variable at an
unobserved location as a weighted sum of the variable at observed
locations. Intuitively, it works as a reverse linear regression: instead
of computing correlation (univariate regression coefficients are simply
scaled correlation) between a dependent variable Y and independent
variables X, it uses known correlation between X and Y to predict Y.

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
