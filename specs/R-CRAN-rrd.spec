%global packname  rrd
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          2%{?dist}
Summary:          Import Data from a RRD (Round Robin Database) File

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    rrdtool-devel
Requires:         rrdtool
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-tibble 

%description
Makes it easy to import the data from a 'RRD' database
(<https://oss.oetiker.ch/rrdtool/>) directly into R data structures. The
resulting objects are 'tibble' objects or a list of 'tibble' objects,
making it easy to manipulate the data.  The package uses `librrd` to
import the numerical data in a `RRD` database directly into R data
structures without using intermediate formats.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
