%global __brp_check_rpaths %{nil}
%global packname  StatDA
%global packver   1.7.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.4
Release:          3%{?dist}%{?buildtag}
Summary:          Statistical Analysis for Environmental Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sgeostat 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-MBA 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-geoR 
Requires:         R-methods 
Requires:         R-CRAN-sgeostat 
Requires:         R-cluster 
Requires:         R-CRAN-e1071 
Requires:         R-MASS 
Requires:         R-CRAN-MBA 
Requires:         R-mgcv 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-geoR 

%description
Several tools are provided for the statistical analysis of environmental
data.

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
%{rlibdir}/%{packname}/INDEX
