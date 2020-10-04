%global packname  yager
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Yet Another General Regression Neural Network

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-datasets 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-CRAN-MLmetrics 
BuildRequires:    R-graphics 
BuildRequires:    R-parallel 
Requires:         R-datasets 
Requires:         R-stats 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-lhs 
Requires:         R-CRAN-MLmetrics 
Requires:         R-graphics 
Requires:         R-parallel 

%description
Another implementation of general regression neural network in R based on
Specht (1991) <DOI:10.1109/72.97934>. It is applicable to the functional
approximation or the classification.

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
