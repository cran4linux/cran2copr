%global packname  SILM
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Simultaneous Inference for Linear Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-scalreg 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-hdi 
BuildRequires:    R-CRAN-SIS 
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
BuildRequires:    R-utils 
Requires:         R-CRAN-scalreg 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-hdi 
Requires:         R-CRAN-SIS 
Requires:         R-stats 
Requires:         R-parallel 
Requires:         R-utils 

%description
Simultaneous inference procedures for high-dimensional linear models as
described by Zhang, X., and Cheng, G. (2017)
<doi:10.1080/01621459.2016.1166114>.

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
