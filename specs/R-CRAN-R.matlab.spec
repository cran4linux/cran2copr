%global packname  R.matlab
%global packver   3.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.6.2
Release:          1%{?dist}
Summary:          Read and Write MAT Files and Call MATLAB from Within R

License:          LGPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R.utils >= 2.5.0
BuildRequires:    R-CRAN-R.methodsS3 >= 1.7.1
BuildRequires:    R-CRAN-R.oo >= 1.21.0
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-R.utils >= 2.5.0
Requires:         R-CRAN-R.methodsS3 >= 1.7.1
Requires:         R-CRAN-R.oo >= 1.21.0
Requires:         R-methods 
Requires:         R-utils 

%description
Methods readMat() and writeMat() for reading and writing MAT files.  For
user with MATLAB v6 or newer installed (either locally or on a remote
host), the package also provides methods for controlling MATLAB
(trademark) via R and sending and retrieving data between R and MATLAB.

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
%doc %{rlibdir}/%{packname}/externals
%doc %{rlibdir}/%{packname}/java
%doc %{rlibdir}/%{packname}/mat-files
%{rlibdir}/%{packname}/INDEX
