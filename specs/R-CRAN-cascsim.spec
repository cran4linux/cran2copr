%global __brp_check_rpaths %{nil}
%global packname  cascsim
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          3%{?dist}%{?buildtag}
Summary:          Casualty Actuarial Society Individual Claim Simulator

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-R2HTML 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-R2HTML 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-methods 

%description
It is an open source insurance claim simulation engine sponsored by the
Casualty Actuarial Society. It generates individual insurance claims
including open claims, reopened claims, incurred but not reported claims
and future claims. It also includes claim data fitting functions to help
set simulation assumptions. It is useful for claim level reserving
analysis. Parodi (2013)
<https://www.actuaries.org.uk/documents/triangle-free-reserving-non-traditional-framework-estimating-reserves-and-reserve-uncertainty>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
