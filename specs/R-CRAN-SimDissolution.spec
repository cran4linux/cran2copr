%global packname  SimDissolution
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Modeling and Assessing Similarity of Drug Dissolutions Profiles

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-alabama 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-graphics 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-alabama 
Requires:         R-CRAN-mvtnorm 
Requires:         R-graphics 

%description
Implementation of a model-based bootstrap approach for testing whether two
formulations are similar. The package provides a function for fitting a
pharmacokinetic model to time-concentration data and comparing the results
for all five candidate models regarding the Residual Sum of Squares (RSS).
The candidate set contains a First order, Hixson-Crowell, Higuchi, Weibull
and a logistic model. The assessment of similarity implemented in this
package is performed regarding the maximum deviation of the profiles. See
Moellenhoff et al. (2018) <doi:10.1002/sim.7689> for details.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
