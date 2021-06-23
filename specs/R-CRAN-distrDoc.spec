%global __brp_check_rpaths %{nil}
%global packname  distrDoc
%global packver   2.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.8.0
Release:          3%{?dist}%{?buildtag}
Summary:          Documentation for 'distr' Family of R Packages

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-distr >= 2.2.0
BuildRequires:    R-CRAN-distrEx >= 2.2.0
BuildRequires:    R-CRAN-distrSim >= 2.2.0
BuildRequires:    R-CRAN-distrTEst >= 2.2.0
BuildRequires:    R-CRAN-distrTeach >= 2.2.0
BuildRequires:    R-CRAN-distrMod >= 2.2.0
BuildRequires:    R-CRAN-RandVar >= 0.7
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-startupmsg 
Requires:         R-CRAN-distr >= 2.2.0
Requires:         R-CRAN-distrEx >= 2.2.0
Requires:         R-CRAN-distrSim >= 2.2.0
Requires:         R-CRAN-distrTEst >= 2.2.0
Requires:         R-CRAN-distrTeach >= 2.2.0
Requires:         R-CRAN-distrMod >= 2.2.0
Requires:         R-CRAN-RandVar >= 0.7
Requires:         R-MASS 
Requires:         R-methods 
Requires:         R-CRAN-startupmsg 

%description
Provides documentation in form of a common vignette to packages 'distr',
'distrEx', 'distrMod', 'distrSim', 'distrTEst', 'distrTeach', and
'distrEllipse'.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/TOBEDONE
%{rlibdir}/%{packname}/INDEX
