%global packname  IRkernel
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          2%{?dist}
Summary:          Native R Kernel for the 'Jupyter Notebook'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    python3dist(jupyter-kernel-test)
BuildRequires:    python3dist(ndjson-testrunner)
Requires:         python-jupyter-filesystem
BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 0.9
BuildRequires:    R-CRAN-repr >= 0.4.99
BuildRequires:    R-CRAN-IRdisplay >= 0.3.0.9999
BuildRequires:    R-CRAN-pbdZMQ >= 0.2.1
BuildRequires:    R-CRAN-evaluate >= 0.10
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-digest 
Requires:         R-CRAN-jsonlite >= 0.9
Requires:         R-CRAN-repr >= 0.4.99
Requires:         R-CRAN-IRdisplay >= 0.3.0.9999
Requires:         R-CRAN-pbdZMQ >= 0.2.1
Requires:         R-CRAN-evaluate >= 0.10
Requires:         R-methods 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-digest 

%description
The R kernel for the 'Jupyter' environment executes R code which the
front-end ('Jupyter Notebook' or other front-ends) submits to the kernel
via the network.

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
%doc %{rlibdir}/%{packname}/kernelspec
%{rlibdir}/%{packname}/INDEX
