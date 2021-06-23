%global __brp_check_rpaths %{nil}
%global packname  AlphaPart
%global packver   0.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.1
Release:          3%{?dist}%{?buildtag}
Summary:          Partition/Decomposition of Breeding Values by Paths ofInformation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-gdata >= 2.6.0
BuildRequires:    R-CRAN-pedigree >= 1.3
BuildRequires:    R-CRAN-directlabels >= 1.1
BuildRequires:    R-CRAN-Rcpp >= 0.9.4
BuildRequires:    R-CRAN-ggplot2 >= 0.8.9
BuildRequires:    R-CRAN-reshape 
Requires:         R-CRAN-gdata >= 2.6.0
Requires:         R-CRAN-pedigree >= 1.3
Requires:         R-CRAN-directlabels >= 1.1
Requires:         R-CRAN-Rcpp >= 0.9.4
Requires:         R-CRAN-ggplot2 >= 0.8.9
Requires:         R-CRAN-reshape 

%description
A software that implements a method for partitioning genetic trends to
quantify the sources of genetic gain in breeding programmes. The
partitioning method is described in Garcia-Cortes et al. (2008)
<doi:10.1017/S175173110800205X>. The package includes the main function
AlphaPart for partitioning breeding values and auxiliary functions for
manipulating data and summarizing, visualizing, and saving results.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
