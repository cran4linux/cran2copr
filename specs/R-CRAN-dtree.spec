%global packname  dtree
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          2%{?dist}
Summary:          Decision Trees

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-party 
BuildRequires:    R-CRAN-evtree 
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-CRAN-caret 
Requires:         R-rpart 
Requires:         R-CRAN-party 
Requires:         R-CRAN-evtree 
Requires:         R-CRAN-partykit 
Requires:         R-CRAN-caret 

%description
Combines various decision tree algorithms, plus both linear regression and
ensemble methods into one package. Allows for the use of both continuous
and categorical outcomes. An optional feature is to quantify the
(in)stability to the decision tree methods, indicating when results can be
trusted and when ensemble methods may be preferential.

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
