%global __brp_check_rpaths %{nil}
%global packname  matchMulti
%global packver   1.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.7
Release:          3%{?dist}%{?buildtag}
Summary:          Optimal Multilevel Matching using a Network Algorithm

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-rcbsubset >= 1.1.4
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-coin 
BuildRequires:    R-CRAN-weights 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-Hmisc 
Requires:         R-CRAN-rcbsubset >= 1.1.4
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-coin 
Requires:         R-CRAN-weights 
Requires:         R-CRAN-mvtnorm 
Requires:         R-MASS 
Requires:         R-CRAN-Hmisc 

%description
Performs multilevel matches for data with cluster-level treatments and
individual-level outcomes using a network optimization algorithm.
Functions for checking balance at the cluster and individual levels are
also provided, as are methods for permutation-inference-based outcome
analysis.  Details in Pimentel et al. (2017+), forthcoming in the Annals
of Applied Statistics.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
