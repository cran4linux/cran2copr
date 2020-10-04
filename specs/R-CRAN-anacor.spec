%global debug_package %{nil}
%global packname  anacor
%global packver   1.1-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Simple and Canonical Correspondence Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-splines 
BuildRequires:    R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-car 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-fda 
Requires:         R-splines 
Requires:         R-grDevices 

%description
Performs simple and canonical CA (covariates on rows/columns) on a two-way
frequency table (with missings) by means of SVD. Different scaling methods
(standard, centroid, Benzecri, Goodman) as well as various plots including
confidence ellipsoids are provided.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
