%global __brp_check_rpaths %{nil}
%global packname  RNetLogo
%global packver   1.0-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          3%{?dist}%{?buildtag}
Summary:          Provides an Interface to the Agent-Based Modelling Platform'NetLogo'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel >= 3.3.2
Requires:         R-core >= 3.3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-rJava >= 0.9.8
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-rJava >= 0.9.8
Requires:         R-CRAN-igraph 

%description
Interface to use and access Wilensky's 'NetLogo' (Wilensky 1999) from R
using either headless (no GUI) or interactive GUI mode. Provides functions
to load models, execute commands, and get values from reporters. Mostly
analogous to the 'NetLogo' 'Mathematica' Link
<https://github.com/NetLogo/Mathematica-Link>.

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
%doc %{rlibdir}/%{packname}/gpl-2.0.txt
%doc %{rlibdir}/%{packname}/java
%doc %{rlibdir}/%{packname}/KnownIssues.log
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/quickStartGuide.txt
%doc %{rlibdir}/%{packname}/WishList.txt
%{rlibdir}/%{packname}/INDEX
