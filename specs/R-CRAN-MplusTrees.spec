%global packname  MplusTrees
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}
Summary:          Decision Trees with Structural Equation Models Fit in 'Mplus'

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-MplusAutomation 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-rpart.plot 
Requires:         R-rpart 
Requires:         R-CRAN-MplusAutomation 
Requires:         R-nlme 
Requires:         R-CRAN-rpart.plot 

%description
Uses recursive partitioning to create homogeneous subgroups based on
structural equation models fit in 'Mplus', a stand-alone program developed
by Muthen and Muthen.

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
