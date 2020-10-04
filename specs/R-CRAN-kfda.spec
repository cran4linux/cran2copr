%global packname  kfda
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Kernel Fisher Discriminant Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-MASS 
Requires:         R-CRAN-kernlab 
Requires:         R-MASS 

%description
Kernel Fisher Discriminant Analysis (KFDA) is performed using Kernel
Principal Component Analysis (KPCA) and Fisher Discriminant Analysis
(FDA). There are some similar packages. First, 'lfda' is a package that
performs Local Fisher Discriminant Analysis (LFDA) and performs other
functions. In particular, 'lfda' seems to be impossible to test because it
needs the label information of the data in the function argument. Also,
the 'ks' package has a limited dimension, which makes it difficult to
analyze properly. This package is a simple and practical package for KFDA
based on the paper of Yang, J., Jin, Z., Yang, J. Y., Zhang, D., and
Frangi, A. F. (2004) <DOI:10.1016/j.patcog.2003.10.015>.

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
%{rlibdir}/%{packname}/INDEX
