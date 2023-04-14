%global __brp_check_rpaths %{nil}
%global packname  phia
%global packver   0.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Post-Hoc Interaction Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-car 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-Matrix 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-car 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-Matrix 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-utils 

%description
Analysis of terms in linear, generalized and mixed linear models, on the
basis of multiple comparisons of factor contrasts.  Specially suited for
the analysis of interaction terms.

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
