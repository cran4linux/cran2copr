%global packname  UNPaC
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}
Summary:          Non-Parametric Cluster Significance Testing with Reference to aUnimodal Null Distribution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-huge 
BuildRequires:    R-CRAN-PDSCE 
Requires:         R-CRAN-huge 
Requires:         R-CRAN-PDSCE 

%description
Assess the significance of identified clusters and estimates the true
number of clusters by comparing the explained variation due to the
clustering from the original data to that produced by clustering a
unimodal reference distribution which preserves the covariance structure
in the data. The reference distribution is generated using kernel density
estimation and a Gaussian copula framework. A dimension reduction strategy
and sparse covariance estimation optimize this method for the
high-dimensional, low-sample size setting. This method is similar to them
method described in Helgeson and Bair (2016) <arXiv:1610.01424> except a
Gaussian copula approach is used to account for feature correlation.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
