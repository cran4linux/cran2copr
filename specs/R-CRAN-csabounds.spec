%global packname  csabounds
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Bounds on Distributional Treatment Effect Parameters

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-BMisc 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-qte 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-BMisc 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-qte 

%description
The joint distribution of potential outcomes is not typically identified
under standard identifying assumptions such as selection on observables or
even when individuals are randomly assigned to being treated. This package
contains methods for obtaining tight bounds on distributional treatment
effect parameters when panel data is available and under a Copula
Stability Assumption as in Callaway (2017)
<https://ssrn.com/abstract=3028251>.

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
