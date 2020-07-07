%global packname  tfse
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          3%{?dist}
Summary:          Tools for Script Editing

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dapr 
BuildRequires:    R-stats 
Requires:         R-utils 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dapr 
Requires:         R-stats 

%description
A collection of useful tools for programming and writing-scripts. Several
functions are simple wrappers around base R functions that extend their
functionality while also providing some convenient properties–regular
expression functions that automatically detect look-ahead and look-behind
statements, a read-line function that suppresses incomplete-final-line
warnings and automatically opens and closes connections, a version of
substrings that starts from the end of strings, etc. Other functions are
useful for checking whether packages are installed, omitting missing data,
and showing in-use connections.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
