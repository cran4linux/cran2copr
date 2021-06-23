%global __brp_check_rpaths %{nil}
%global packname  packHV
%global packver   2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2
Release:          3%{?dist}%{?buildtag}
Summary:          A few Useful Functions for Statisticians

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-WriteXLS >= 2.3.0
BuildRequires:    R-survival 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-WriteXLS >= 2.3.0
Requires:         R-survival 
Requires:         R-stats 
Requires:         R-graphics 

%description
Various useful functions for statisticians: describe data, plot
Kaplan-Meier curves with numbers of subjects at risk, compare data sets,
display spaghetti-plot, build multi-contingency tables...

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
