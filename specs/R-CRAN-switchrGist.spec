%global packname  switchrGist
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}
Summary:          Publish Package Manifests to GitHub Gists

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-switchr >= 0.9.4
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-gistr 
BuildRequires:    R-CRAN-httpuv 
BuildRequires:    R-CRAN-RJSONIO 
Requires:         R-CRAN-switchr >= 0.9.4
Requires:         R-methods 
Requires:         R-CRAN-gistr 
Requires:         R-CRAN-httpuv 
Requires:         R-CRAN-RJSONIO 

%description
Provides a simple plugin to the switchr framework which allows users to
publish package and session manifests as gists.

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
%{rlibdir}/%{packname}/INDEX
