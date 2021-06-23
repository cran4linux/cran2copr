%global __brp_check_rpaths %{nil}
%global packname  TSDT
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Treatment-Specific Subgroup Detection Tool

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mlbench 
BuildRequires:    R-CRAN-hash 
BuildRequires:    R-CRAN-party 
BuildRequires:    R-rpart 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-survRM2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-modeltools 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
Requires:         R-methods 
Requires:         R-CRAN-mlbench 
Requires:         R-CRAN-hash 
Requires:         R-CRAN-party 
Requires:         R-rpart 
Requires:         R-survival 
Requires:         R-CRAN-survRM2 
Requires:         R-stats 
Requires:         R-CRAN-modeltools 
Requires:         R-utils 
Requires:         R-parallel 

%description
Implements a method for identifying subgroups with superior response
relative to the overall sample.

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
