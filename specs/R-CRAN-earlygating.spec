%global packname  earlygating
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Properties of Bayesian Early Gating Designs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-betareg 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-betareg 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 

%description
Computes the most important properties of four 'Bayesian' early gating
designs (two single arm and two randomized controlled designs), such as
minimum required number of successes in the experimental group to make a
GO decision, operating characteristics and average operating
characteristics with respect to the sample size. These might aid in
deciding what design to use for the early phase trial.

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
