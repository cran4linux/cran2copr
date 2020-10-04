%global packname  loopr
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Uses an Archive to Amend Previous Stages of a Pipe using CurrentOutput

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.3
Requires:         R-core >= 3.1.3
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.0.1
BuildRequires:    R-CRAN-plyr >= 1.8.1
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-dplyr >= 0.4.1
BuildRequires:    R-CRAN-lazyeval >= 0.1.10
Requires:         R-CRAN-R6 >= 2.0.1
Requires:         R-CRAN-plyr >= 1.8.1
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-dplyr >= 0.4.1
Requires:         R-CRAN-lazyeval >= 0.1.10

%description
Remedies a common problem in piping: not having access to intermediate
outputs of the pipe. Within a "loop", a piping intermediate is stored in a
stack archive, data is processed, and then both the stored intermediate
and the current output are reintegrated using an "ending" function. Two
special ending functions are provided: amend and insert. However, any
ending function can be specified, including merge functions, join
functions, setNames(), etc. This framework allows the following work-flow:
focus on a particular aspect or section of a data set, conduct specific
operations, and then reintegrate changes into the whole.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
