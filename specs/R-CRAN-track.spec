%global __brp_check_rpaths %{nil}
%global packname  track
%global packver   1.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.9
Release:          3%{?dist}%{?buildtag}
Summary:          Store Objects on Disk Automatically

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.1.0
Requires:         R-core >= 2.1.0
BuildArch:        noarch
BuildRequires:    R-methods 
Requires:         R-methods 

%description
Automatically stores objects in files on disk so that files are rewritten
when objects are changed, and so that objects are accessible but do not
occupy memory until they are accessed. Keeps track of times when objects
are created and modified, and caches some basic characteristics of objects
to allow for fast summaries of objects.  Also provides a command history
mechanism that saves the last command to a history file after each command
completes.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/performanceTrials
%doc %{rlibdir}/%{packname}/sccversion.txt
%doc %{rlibdir}/%{packname}/svnversion.txt
%{rlibdir}/%{packname}/INDEX
