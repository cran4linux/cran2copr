%global packname  np
%global packver   0.60-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.60.9
Release:          1%{?dist}
Summary:          Nonparametric Kernel Smoothing Methods for Mixed Data Types

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-stats 
Requires:         R-boot 
Requires:         R-CRAN-cubature 
Requires:         R-methods 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-quantreg 
Requires:         R-stats 

%description
Nonparametric (and semiparametric) kernel methods that seamlessly handle a
mix of continuous, unordered, and ordered factor data types. We would like
to gratefully acknowledge support from the Natural Sciences and
Engineering Research Council of Canada (NSERC,
<http://www.nserc-crsng.gc.ca>), the Social Sciences and Humanities
Research Council of Canada (SSHRC, <http://www.sshrc-crsh.gc.ca>), and the
Shared Hierarchical Academic Research Computing Network (SHARCNET,
<http://www.sharcnet.ca>).

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
%{rlibdir}/%{packname}/data
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/kernels.max
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
