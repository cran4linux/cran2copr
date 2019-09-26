%global packname  ccfa
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Continuous Counterfactual Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.1.0
Requires:         R-core >= 2.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-BMisc 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-TempleMetrics 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-formula.tools 
Requires:         R-CRAN-quantreg 
Requires:         R-stats 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-BMisc 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-TempleMetrics 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-formula.tools 

%description
Contains methods for computing counterfactuals with a continuous treatment
variable as in Callaway and Huang (2017)
<https://ssrn.com/abstract=3078187>.  In particular, the package can be
used to calculate the expected value, the variance, the interquantile
range, the fraction of observations below or above a particular cutoff, or
other user-supplied functions of an outcome of interest conditional on a
continuous treatment.  The package can also be used for computing these
same functionals after adjusting for differences in covariates at
different values of the treatment.  Further, one can use the package to
conduct uniform inference for each parameter of interest across all values
of the treatment, uniformly test whether adjusting for covariates makes a
difference at any value of the treatment, and test whether a parameter of
interest is different from its average value at an value of the treatment.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
