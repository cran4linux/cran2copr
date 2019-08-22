%global packname  CAMAN
%global packver   0.74
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.74
Release:          1%{?dist}
Summary:          Finite Mixture Models and Meta-Analysis Tools - Based on C.A.MAN

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-methods 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-mvtnorm 

%description
Tools for the analysis of finite semiparametric mixtures. These are useful
when data is heterogeneous, e.g. in pharmacokinetics or meta-analysis. The
NPMLE and VEM algorithms (flexible support size) and EM algorithms (fixed
support size) are provided for univariate and bivariate data.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
