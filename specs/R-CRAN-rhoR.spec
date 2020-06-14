%global packname  rhoR
%global packver   1.3.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0.2
Release:          2%{?dist}
Summary:          Rho for Inter Rater Reliability

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 

%description
Rho is used to test the generalization of inter rater reliability (IRR)
statistics. Calculating rho starts by generating a large number of
simulated, fully-coded data sets: a sizable collection of hypothetical
populations, all of which have a kappa value below a given threshold --
which indicates unacceptable agreement. Then kappa is calculated on a
sample from each of those sets in the collection to see if it is equal to
or higher than the kappa in then real sample. If less than five percent of
the distribution of samples from the simulated data sets is greater than
actual observed kappa, the null hypothesis is rejected and one can
conclude that if the two raters had coded the rest of the data, we would
have acceptable agreement (kappa above the threshold).

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/_pkgdown.yml
%doc %{rlibdir}/%{packname}/coverage
%doc %{rlibdir}/%{packname}/docker
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
