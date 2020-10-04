%global debug_package %{nil}
%global packname  ITRSelect
%global packver   1.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Variable Selection for Optimal Individualized Dynamic TreatmentRegime

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-Rglpk 
BuildRequires:    R-CRAN-ncvreg 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-svMisc 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-Rglpk 
Requires:         R-CRAN-ncvreg 
Requires:         R-Matrix 
Requires:         R-CRAN-svMisc 

%description
Sequential advantage selection (SAS, Fan, Lu and Song, 2016)
<arXiv:1405.5239> and penalized A-learning (PAL, Shi, et al., 2018)
methods are implement for selecting important variables involved in
optimal individualized (dynamic) treatment regime in both single-stage or
multi-stage studies.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
