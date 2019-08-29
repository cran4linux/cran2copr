%global packname  BLOQ
%global packver   0.1-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Impute and Analyze Data with Observations Below the Limit ofQuantification

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-mvnmle 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-mvnmle 
Requires:         R-CRAN-mvtnorm 

%description
Methods for non-compartmental pharmacokinetic analysis with observations
below the limit of quantification (BLOQ) are implemented as described in
Barnett, Helen Yvette. "Optimizing pharmacokinetic studies utilizing
microsampling." PhD diss., Lancaster University, 2017. (available online:
<http://eprints.lancs.ac.uk/89163/1/2017barnettphd.pdf>). It includes
estimating the area under the concentrations versus time curve (AUC) and
its standard error using two approaches: direct estimation using censored
maximum likelihood, also by first imputing the BLOQ's using various
methods, then compute AUC and its standard error using imputed data.

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
