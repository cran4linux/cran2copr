%global __brp_check_rpaths %{nil}
%global packname  distantia
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Assessing Dissimilarity Between Multivariate Time Series

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-arrangements 
Requires:         R-CRAN-plyr 
Requires:         R-grDevices 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-arrangements 

%description
Provides tools to assess the dissimilarity between multivariate
time-series. It is based on the psi measure described by Birks and Gordon
(1985 <doi:10.1002/jqs.3390020110>), which computes dissimilarity between
irregular time-series constrained by sample order. However, in this
package the original idea has been extended to work with any kind of
multivariate time-series, no matter whether they are regular, irregular,
aligned or unaligned. Furthermore, the package allows to assess the
significance of dissimilarity values by applying a restricted permutation
test, allows to measure the contribution of individual variables to
dissimilarity, and offers tools to transfer attributes (generally time or
age, but other are possible) between sequences based on the similarity of
their samples.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
