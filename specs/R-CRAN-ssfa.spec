%global packname  ssfa
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Spatial Stochastic Frontier Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-sp 
Requires:         R-Matrix 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-sp 

%description
Spatial Stochastic Frontier Analysis (SSFA) is an original method for
controlling the spatial heterogeneity in Stochastic Frontier Analysis
(SFA) models, for cross-sectional data, by splitting the inefficiency term
into three terms: the first one related to spatial peculiarities of the
territory in which each single unit operates, the second one related to
the specific production features and the third one representing the error
term.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
