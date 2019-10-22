%global packname  switchr
%global packver   0.13.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.13.5
Release:          1%{?dist}
Summary:          Installing, Managing, and Switching Between Distinct Sets ofInstalled Packages

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         git
Requires:         subversion
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-RJSONIO 
BuildRequires:    R-CRAN-RCurl 
Requires:         R-methods 
Requires:         R-tools 
Requires:         R-CRAN-RJSONIO 
Requires:         R-CRAN-RCurl 

%description
Provides an abstraction for managing, installing, and switching between
sets of installed R packages. This allows users to maintain multiple
package libraries simultaneously, e.g. to maintain strict,
package-version-specific reproducibility of many analyses, or work within
a development/production release paradigm. Introduces a generalized
package installation process which supports multiple repository and
non-repository sources and tracks package provenance.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/localcheckoutest.R
%doc %{rlibdir}/%{packname}/ropensciman.R
%doc %{rlibdir}/%{packname}/talks
%doc %{rlibdir}/%{packname}/testlimma.R
%doc %{rlibdir}/%{packname}/xtable.R
%{rlibdir}/%{packname}/INDEX
